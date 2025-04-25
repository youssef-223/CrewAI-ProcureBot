from crewai.tools import tool
from tavily import TavilyClient
from scrapegraph_py import Client
from src.models import SingleExtractedProduct
import os

# Initialize clients
search_client = None
scrape_client = None

def init_tools(tavily_api_key, scrapegraph_api_key):
    """Initialize the tools with API keys"""
    global search_client, scrape_client
    search_client = TavilyClient(api_key=tavily_api_key)
    scrape_client = Client(api_key=scrapegraph_api_key)

@tool
def search_engine_tool(query: str):
    """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
    if not search_client:
        raise ValueError("Search client not initialized. Call init_tools first.")
    return search_client.search(query)

@tool
def web_scraping_tool(page_url: str):
    """
    An AI Tool to help an agent to scrape a web page

    Example:
    web_scraping_tool(
        page_url="https://www.noon.com/egypt-en/15-bar-fully-automatic-espresso-machine-1-8-l-1500"
    )
    """
    if not scrape_client:
        raise ValueError("Scrape client not initialized. Call init_tools first.")
        
    details = scrape_client.smartscraper(
        website_url=page_url,
        user_prompt="Extract ```json\n" + SingleExtractedProduct.schema_json() + "```\n From the web page"
    )

    return {
        "page_url": page_url,
        "details": details
    } 