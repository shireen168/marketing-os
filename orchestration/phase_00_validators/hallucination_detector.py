"""Hallucination Detector: Self-audit engine for fact-checking research reports."""

import re
from typing import List, Dict, Any
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class HallucinationDetector:
    """
    Validates research reports for unsourced claims, citation quality, and contradictions.

    Methods:
    - detect_unsourced_claims: Find claims without citations
    - check_citation_count: Validate minimum citation count
    - check_source_dates: Flag outdated sources (>180 days old)
    - detect_contradictions: Find contradictory data across sections
    """

    def __init__(self):
        """Initialize the Hallucination Detector."""
        # Regex to extract numbers: dollar amounts ($2.5B), percentages (8%), years (2025)
        self.number_pattern = r'\$[\d.]+[BM]|\d+%|\d{4}(?:\d{2})?'
        self.outdated_threshold_days = 180  # 6 months

    def detect_unsourced_claims(self, text: str, citations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Detect claims in text that are not supported by citations.

        Args:
            text: The research text to analyze
            citations: List of citation dicts with url, date, excerpt, source

        Returns:
            List of issue dicts: {claim: str, type: str, severity: str}
        """
        if not text or not citations:
            return []

        issues = []

        # Extract all numbers (dollar amounts, percentages, years) from text
        numbers_in_text = re.findall(self.number_pattern, text)
        if not numbers_in_text:
            return issues

        # Extract numbers from all citation excerpts
        cited_numbers = set()
        for citation in citations:
            excerpt = citation.get("excerpt", "").lower()
            cited_nums = re.findall(self.number_pattern, excerpt)
            cited_numbers.update(cited_nums)

        # Find uncited numbers
        for number in set(numbers_in_text):
            if number.lower() not in cited_numbers:
                # Extract context around the number
                pattern = re.compile(re.escape(number) + r'[^.!?]*[.!?]?', re.IGNORECASE)
                matches = pattern.findall(text)
                if matches:
                    claim_context = matches[0].strip()
                    issues.append({
                        "claim": claim_context,
                        "number": number,
                        "type": "unsourced_claim",
                        "severity": "high"
                    })

        logger.info(f"Detected {len(issues)} unsourced claims in text")
        return issues

    def check_citation_count(
        self,
        citations: List[Dict[str, Any]],
        min_required: int
    ) -> Dict[str, Any]:
        """
        Validate that citation count meets minimum threshold.

        Args:
            citations: List of citation dicts
            min_required: Minimum number of citations required

        Returns:
            Dict with keys: {pass: bool, count: int, required: int, message: str}
        """
        count = len(citations)
        passed = count >= min_required

        if passed:
            message = f"Citation count ({count}) meets minimum requirement ({min_required})"
        else:
            message = f"Insufficient citations: {count} found, {min_required} required"

        result = {
            "pass": passed,
            "count": count,
            "required": min_required,
            "message": message
        }

        logger.info(f"Citation count check: {message}")
        return result

    def check_source_dates(self, citations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Check citation dates and flag sources older than 180 days.

        Args:
            citations: List of citation dicts with date field (YYYY-MM-DD format)

        Returns:
            List of dicts: {url: str, date: str, is_recent: bool, warning: str or None}
        """
        if not citations:
            return []

        results = []
        today = datetime.now()
        threshold_date = today - timedelta(days=self.outdated_threshold_days)

        for citation in citations:
            url = citation.get("url", "")
            date_str = citation.get("date", "")

            # Parse date (handle YYYY-MM-DD format)
            try:
                citation_date = datetime.strptime(date_str, "%Y-%m-%d")
                is_recent = citation_date >= threshold_date
                days_old = (today - citation_date).days

                warning = None
                if not is_recent:
                    warning = f"Source is {days_old} days old (exceeds {self.outdated_threshold_days} day threshold)"

                results.append({
                    "url": url,
                    "date": date_str,
                    "is_recent": is_recent,
                    "days_old": days_old,
                    "warning": warning
                })

            except (ValueError, TypeError):
                # Handle invalid date format
                results.append({
                    "url": url,
                    "date": date_str,
                    "is_recent": False,
                    "days_old": None,
                    "warning": f"Invalid date format: {date_str}"
                })

        logger.info(f"Checked {len(results)} sources for date recency")
        return results

    def detect_contradictions(self, sections: Dict[str, str]) -> List[Dict[str, Any]]:
        """
        Detect contradictions (same number appearing with different contexts) across sections.

        Args:
            sections: Dict of {section_name: section_text}

        Returns:
            List of contradiction dicts: {number: str, contexts: List[str], severity: str}
        """
        if not sections:
            return []

        issues = []

        # Extract numbers from each section
        section_numbers = {}
        for section_name, section_text in sections.items():
            numbers = re.findall(self.number_pattern, section_text)
            section_numbers[section_name] = {
                "numbers": numbers,
                "text": section_text
            }

        # Find numbers that appear in multiple sections
        all_numbers = {}
        for section_name, data in section_numbers.items():
            for number in data["numbers"]:
                if number not in all_numbers:
                    all_numbers[number] = []
                all_numbers[number].append(section_name)

        # Detect contradictions: same number in different sections with different context
        for number, sections_list in all_numbers.items():
            if len(sections_list) > 1:
                # Collect contexts for this number across sections
                contexts = []
                for section_name in sections_list:
                    section_text = section_numbers[section_name]["text"]
                    # Extract sentence containing the number
                    pattern = re.compile(r'[^.!?]*' + re.escape(number) + r'[^.!?]*[.!?]?', re.IGNORECASE)
                    matches = pattern.findall(section_text)
                    if matches:
                        context = matches[0].strip()
                        contexts.append({
                            "section": section_name,
                            "context": context
                        })

                # If same number appears in different contexts, it's a contradiction
                if len(contexts) > 1:
                    # Check if contexts are significantly different (simple heuristic)
                    context_texts = [c["context"].lower() for c in contexts]
                    if len(set(context_texts)) > 1:
                        issues.append({
                            "number": number,
                            "contexts": contexts,
                            "type": "contradiction",
                            "severity": "high"
                        })

        logger.info(f"Detected {len(issues)} potential contradictions")
        return issues
