"""Citation Builder: Format research citations into markdown structures."""

from typing import List, Dict, Any


class CitationBuilder:
    """
    Formats citation data into markdown structures for research reports.

    Supports:
    - Markdown tables with citations
    - Inline citation format
    - Reference sections grouped by source
    """

    def __init__(self):
        """Initialize the Citation Builder."""
        pass

    def to_markdown_table(self, citations: List[Dict[str, Any]]) -> str:
        """
        Format citations as a markdown table.

        Args:
            citations: List of citation dictionaries with url, date, excerpt, score, source

        Returns:
            Markdown table string with format: | URL | Date | Excerpt | Score | Source |
        """
        if not citations:
            return ""

        # Header
        lines = [
            "| URL | Date | Excerpt | Score | Source |",
            "|---|---|---|---|---|",
        ]

        # Rows
        for citation in citations:
            url = citation.get("url", "")
            date = citation.get("date", "")
            excerpt = citation.get("excerpt", "")
            score = citation.get("score", 0)
            source = citation.get("source", "")

            # Truncate URL to max 50 chars
            url_display = self._truncate(url, 50)

            # Truncate excerpt to max 200 chars
            excerpt_display = self._truncate(excerpt, 200)

            # Format score with 2 decimal places
            score_display = f"{float(score):.2f}"

            # Escape pipes and newlines in cell content
            url_display = url_display.replace("|", "\\|").replace("\n", " ")
            excerpt_display = excerpt_display.replace("|", "\\|").replace("\n", " ")

            row = f"| {url_display} | {date} | {excerpt_display} | {score_display} | {source} |"
            lines.append(row)

        return "\n".join(lines)

    def to_inline(self, citation: Dict[str, Any]) -> str:
        """
        Format a single citation as inline text.

        Format: (Source: URL, Date: YYYY-MM-DD)

        Args:
            citation: Citation dictionary with url, date, source, and optionally excerpt

        Returns:
            Formatted inline citation string
        """
        url = citation.get("url", "")
        date = citation.get("date", "")
        source = citation.get("source", "")

        # Truncate URL to max 50 chars for inline format
        url_display = self._truncate(url, 50)

        return f"(Source: {url_display}, Date: {date})"

    def reference_section(self, citations: List[Dict[str, Any]]) -> str:
        """
        Build a full reference section grouped by source.

        Groups citations by source (tavily first, then perplexity), with each citation
        formatted as a list item with url, date, and excerpt.

        Args:
            citations: List of citation dictionaries

        Returns:
            Formatted reference section string
        """
        if not citations:
            return ""

        # Group by source
        grouped = {}
        for citation in citations:
            source = citation.get("source", "unknown")
            if source not in grouped:
                grouped[source] = []
            grouped[source].append(citation)

        # Build reference section with tavily first, then perplexity, then others
        source_order = ["tavily", "perplexity"]
        other_sources = [s for s in grouped.keys() if s not in source_order]
        ordered_sources = source_order + other_sources

        lines = ["## References"]

        for source in ordered_sources:
            if source not in grouped:
                continue

            # Source header
            lines.append(f"\n### {source.capitalize()}")

            # Citations for this source
            for citation in grouped[source]:
                url = citation.get("url", "")
                date = citation.get("date", "")
                excerpt = citation.get("excerpt", "")

                # Format: - [URL](URL) — Date: YYYY-MM-DD. Excerpt: excerpt_text
                url_display = self._truncate(url, 50)
                excerpt_display = self._truncate(excerpt, 200)

                citation_line = f"- [{url_display}]({url}) — Date: {date}"
                if excerpt_display:
                    citation_line += f". Excerpt: {excerpt_display}"

                lines.append(citation_line)

        return "\n".join(lines)

    def _truncate(self, text: str, max_length: int) -> str:
        """
        Truncate text to max length, adding ellipsis if truncated.

        Args:
            text: Text to truncate
            max_length: Maximum length

        Returns:
            Truncated text with ellipsis if needed
        """
        if not text:
            return ""

        text = str(text).strip()
        if len(text) <= max_length:
            return text

        return text[: max_length - 3] + "..."
