"""Real research fetcher using Tavily and Claude APIs."""

import os
import json
import asyncio
import sys
from typing import Any
from pathlib import Path
from dotenv import load_dotenv

try:
    import requests
    from anthropic import Anthropic
except ImportError as e:
    print(f"Missing required packages. Run: pip install -r orchestration/requirements.txt")
    print(f"Error: {e}")
    sys.exit(1)

# Load .env file
env_path = Path(__file__).parent.parent.parent / "orchestration" / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    # Try alternate path
    load_dotenv()


class RealResearchFetcher:
    """Fetch real market research using Tavily API and synthesize with Claude."""

    def __init__(self):
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        self.anthropic_client = Anthropic()
        self.tavily_base_url = "https://api.tavily.com/search"

    def fetch_tavily_research(self, query: str, max_results: int = 10) -> list[dict]:
        """Fetch research results from Tavily API."""
        if not self.tavily_api_key:
            return []

        try:
            payload = {
                "api_key": self.tavily_api_key,
                "query": query,
                "max_results": max_results,
                "include_answer": True,
            }
            response = requests.post(self.tavily_base_url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except Exception as e:
            print(f"Tavily API error: {e}")
            return []

    def synthesize_research(
        self,
        product_name: str,
        research_queries: dict[str, list[str]],
        research_results: dict[str, list[dict]],
    ) -> str:
        """Synthesize research results into a comprehensive report using Claude."""

        # Build research summary with URLs for Claude
        research_summary = self._build_research_summary_with_urls(research_queries, research_results)

        # Use Claude to synthesize
        prompt = f"""You are a market research analyst. Synthesize the following research findings into a professional market research report for a smart sleep device.

Product: {product_name}
Target Audiences: DTC consumers and healthcare systems
Data Collected: {research_summary}

Create a COMPLETE and COMPREHENSIVE 50+ page research report (in markdown) with ALL sections below. DO NOT truncate or abbreviate.

REQUIRED SECTIONS (with minimum page counts):
1. **Executive Summary** (2-3 pages) - Key findings, market opportunity, strategic recommendations, confidence scores
2. **Market Sizing** (6-8 pages) - Detailed TAM/SAM/SOM analysis, CAGR, segment breakdown with financial tables
3. **Customer Segmentation** (8-10 pages) - 5+ detailed personas (DTC and healthcare) with demographics, pain points, budgets, decision makers
4. **Competitive Landscape** (10-12 pages) - 8+ competitor profiles with funding, positioning, strengths, weaknesses, market positioning matrix
5. **Regulatory Assessment** (4-5 pages) - FDA pathways, HIPAA requirements, clinical validation needs, timelines
6. **Market Validation** (3-4 pages) - Validated assumptions vs. risks, market signals, barriers to entry
7. **Key Strategic Insights** (2-3 pages) - 8-10 critical insights from research
8. **Recommended Next Steps** (2-3 pages) - Specific Phase 2 strategy recommendations with rationale
9. **Sources & References** (2-3 pages) - Complete bibliography with all URLs as clickable markdown links

CRITICAL REQUIREMENTS:
- Use real market data from the research findings (include specific numbers)
- Create detailed tables for all market sizing and customer economics
- Include inline citations: [Source Name](URL) for every data point
- Add competitor positioning matrix showing differentiation opportunities
- Include customer segment economics (CAC, LTV, payback period)
- Provide FDA/regulatory timeline with specific 2026 guidance references
- Create a comprehensive "Sources & References" section at end with all URLs

DO NOT TRUNCATE. Generate the COMPLETE 50+ page report with all sections fully developed.
"""

        message = self.anthropic_client.messages.create(
            model="claude-opus-4-7",
            max_tokens=20000,
            messages=[{"role": "user", "content": prompt}],
        )

        return message.content[0].text

    def _build_research_summary(
        self, queries: dict[str, list[str]], results: dict[str, list[dict]]
    ) -> str:
        """Build a summary of research findings for Claude."""
        summary = "Research Findings:\n\n"

        for category, query_list in queries.items():
            summary += f"\n## {category}\n"
            summary += f"Queries: {', '.join(query_list)}\n\n"

            if category in results:
                for result in results[category][:3]:  # Top 3 per category
                    summary += f"- **{result.get('title', 'Untitled')}**\n"
                    summary += f"  {result.get('content', 'No summary')}...\n"
                    summary += f"  Source: {result.get('url', 'Unknown')}\n\n"

        return summary

    def _build_research_summary_with_urls(
        self, queries: dict[str, list[str]], results: dict[str, list[dict]]
    ) -> str:
        """Build research summary with URLs for proper citation in report."""
        summary = "Research Findings with Sources:\n\n"
        urls = []

        for category, query_list in queries.items():
            summary += f"\n## {category}\n"
            summary += f"Queries: {', '.join(query_list)}\n\n"

            if category in results:
                for i, result in enumerate(results[category][:5], 1):  # Top 5 per category
                    title = result.get('title', 'Untitled')
                    url = result.get('url', '')
                    content = result.get('content', 'No summary available')

                    # Create reference format
                    if url:
                        summary += f"- [{title}]({url})\n"
                        summary += f"  {content}...\n\n"
                        urls.append({"title": title, "url": url, "category": category})
                    else:
                        summary += f"- **{title}**\n"
                        summary += f"  {content}...\n\n"

        # Add reference section
        summary += "\n\n## SOURCES & REFERENCES (for citation in report):\n"
        for url_item in urls:
            summary += f"- [{url_item['title']}]({url_item['url']}) ({url_item['category']})\n"

        return summary

    def run_full_research(self, product_name: str, clarifications: dict) -> str:
        """Run complete research workflow."""

        # Define research queries based on clarifications
        research_queries = {
            "Market Sizing": [
                f"{product_name} market size 2025 2026",
                "sleep monitoring device market CAGR growth forecast",
                "wearable health tech market TAM",
            ],
            "Customer Segments": [
                f"{product_name} target customers healthcare wellness",
                "sleep apnea screening market size",
                "corporate wellness sleep program adoption",
            ],
            "Competitors": [
                "Oura Ring vs Whoop vs Fitbit sleep tracking",
                "Apple Watch sleep monitoring capabilities",
                "clinical sleep device market competitors",
            ],
            "Regulatory": [
                "FDA sleep monitoring device regulations classification",
                "HIPAA medical device requirements",
                "clinical sleep study validation standards",
            ],
            "Pricing": [
                "sleep tracker device pricing 2025",
                "wearable health device revenue model SaaS",
                "medical device pricing benchmarks",
            ],
            "Adoption": [
                "sleep tracking app adoption rates 2025",
                "wearable device consumer penetration",
                "healthcare technology adoption barriers",
            ],
        }

        # Fetch research from Tavily
        research_results = {}
        print("Fetching research from Tavily...")
        for category, queries in research_queries.items():
            print(f"  Researching: {category}")
            category_results = []
            for query in queries:
                results = self.fetch_tavily_research(query, max_results=5)
                category_results.extend(results)
            research_results[category] = category_results

        # Synthesize with Claude
        print("Synthesizing research report with Claude...")
        report = self.synthesize_research(product_name, research_queries, research_results)

        return report
