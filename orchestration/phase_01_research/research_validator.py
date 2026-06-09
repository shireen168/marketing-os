"""Research Validator: Tavily + Perplexity integration for real-time web research."""

from typing import List, Dict, Any, Callable, Optional
from datetime import datetime
import re
import requests
import logging

from orchestration.core.config import Config

logger = logging.getLogger(__name__)


class ResearchValidator:
    """
    Fetches real-time research data from Tavily (primary) or Perplexity (fallback).

    Returns structured citations with: [url, date_fetched, excerpt, relevance_score, source]
    """

    def __init__(self):
        """Initialize the Research Validator."""
        self.tavily_api_key = Config.TAVILY_API_KEY
        self.perplexity_api_key = Config.PERPLEXITY_API_KEY
        self.tavily_endpoint = "https://api.tavily.com/search"
        self.perplexity_endpoint = "https://api.perplexity.ai/chat/completions"
        self.tavily_timeout = Config.TAVILY_TIMEOUT
        self.perplexity_timeout = Config.PERPLEXITY_TIMEOUT

    def search_tavily(self, queries: List[str]) -> List[Dict[str, Any]]:
        """
        Fetch research data from Tavily API.

        Args:
            queries: List of search queries

        Returns:
            List of citations with url, date, excerpt, score, source

        Raises:
            requests.RequestException: If Tavily API call fails
            ValueError: If response is missing required fields
        """
        citations = []

        for query in queries:
            try:
                payload = {
                    "api_key": self.tavily_api_key,
                    "query": query,
                    "include_answer": True,
                    "max_results": 5,
                }

                response = requests.post(
                    self.tavily_endpoint,
                    json=payload,
                    timeout=self.tavily_timeout,
                )

                response.raise_for_status()
                data = response.json()

                # Parse Tavily results
                if "results" not in data:
                    logger.warning(f"Tavily response missing 'results' key for query '{query}'")
                    continue

                for result in data["results"]:
                    url = result.get("url", "").strip()
                    content = result.get("content", "").strip()
                    title = result.get("title", "").strip()
                    excerpt = content or title or f"Result for {query}"

                    # Skip results with empty both content and title
                    if not content and not title:
                        logger.warning(f"Skipping result with empty content/title for query '{query}': {url}")
                        continue

                    citation = {
                        "url": url,
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "excerpt": excerpt,
                        "score": result.get("score", 0.8),  # Use API-provided score with fallback
                        "source": "tavily",
                    }
                    citations.append(citation)

            except requests.RequestException as e:
                logger.error(f"Tavily API request error for query '{query}': {e}")
                raise
            except (KeyError, ValueError) as e:
                logger.error(f"Tavily response parsing error for query '{query}': {e}")
                raise

        return citations

    def search_perplexity(self, queries: List[str]) -> List[Dict[str, Any]]:
        """
        Fetch research data from Perplexity API (fallback).

        Args:
            queries: List of search queries

        Returns:
            List of citations with url, date, excerpt, score, source

        Raises:
            requests.RequestException: If Perplexity API call fails
            ValueError: If response format is invalid
        """
        citations = []

        for query in queries:
            try:
                payload = {
                    "model": "pplx-7b-online",
                    "messages": [
                        {
                            "role": "user",
                            "content": f"Search for and provide sources about: {query}. "
                            "Format each source as [URL, brief description]",
                        }
                    ],
                }

                headers = {
                    "Authorization": f"Bearer {self.perplexity_api_key}",
                    "Content-Type": "application/json",
                }

                response = requests.post(
                    self.perplexity_endpoint,
                    json=payload,
                    headers=headers,
                    timeout=self.perplexity_timeout,
                )

                response.raise_for_status()
                data = response.json()

                # Parse Perplexity results
                if "choices" not in data or len(data["choices"]) == 0:
                    logger.warning(f"Perplexity response missing 'choices' for query '{query}'")
                    continue

                content = data["choices"][0].get("message", {}).get("content", "")
                if not content:
                    logger.warning(f"Perplexity response has empty content for query '{query}'")
                    continue

                # Extract URLs using regex for robust parsing: https?://[^\s\],]+
                # The pattern matches http(s):// followed by non-whitespace, non-bracket, non-comma chars
                urls = re.findall(r'https?://[^\s\],]+', content)

                if not urls:
                    logger.debug(f"No URLs found in Perplexity response for query '{query}'")
                    continue

                for url in urls:
                    # Validate URL format
                    if not url.startswith(("http://", "https://")):
                        logger.debug(f"Invalid URL format, skipping: {url}")
                        continue

                    # Try to extract description from content (context around URL)
                    desc = ""
                    lines = content.split("\n")
                    for line in lines:
                        if url in line:
                            # Extract description from the line containing the URL
                            parts = line.split(",", 1)
                            if len(parts) > 1:
                                desc = parts[1].strip().rstrip("]").strip()
                            break

                    citation = {
                        "url": url,
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "excerpt": desc or query,
                        "score": 0.7,  # Conservative default; Perplexity doesn't provide confidence scores
                        "source": "perplexity",
                    }
                    citations.append(citation)

            except requests.RequestException as e:
                logger.error(f"Perplexity API request error for query '{query}': {e}")
                raise
            except (KeyError, ValueError) as e:
                logger.error(f"Perplexity response parsing error for query '{query}': {e}")
                raise

        return citations

    def search_with_fallback(
        self,
        queries: List[str],
        alert_callback: Optional[Callable[[str], None]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Search with Tavily first, fallback to Perplexity on failure.

        Args:
            queries: List of search queries
            alert_callback: Optional callback to alert on fallback

        Returns:
            List of citations from Tavily or Perplexity

        Raises:
            RuntimeError: If both Tavily and Perplexity fail
        """
        # Try Tavily first
        try:
            logger.info("Attempting Tavily search...")
            citations = self.search_tavily(queries)
            logger.info(f"Tavily search successful. Retrieved {len(citations)} citations.")
            return citations

        except Exception as e:
            logger.warning(f"Tavily search failed: {e}. Falling back to Perplexity...")

            # Alert on fallback
            if alert_callback:
                alert_callback(f"Tavily API failed, falling back to Perplexity: {e}")

            # Try Perplexity
            try:
                logger.info("Attempting Perplexity search...")
                citations = self.search_perplexity(queries)
                logger.info(
                    f"Perplexity search successful. Retrieved {len(citations)} citations."
                )
                return citations

            except Exception as perplexity_error:
                logger.error(f"Perplexity search also failed: {perplexity_error}")
                raise RuntimeError(
                    f"Real-time research unavailable. Both Tavily and Perplexity failed. "
                    f"Tavily error: {e}. Perplexity error: {perplexity_error}"
                )
