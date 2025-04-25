from crewai import Agent, LLM
from src.tools import search_engine_tool, web_scraping_tool
from src.models import SuggestedSearchQueries, AllSearchResults, AllExtractedProducts

def create_agents(llm_model="gpt-4o", temperature=0):
    """Create all agents needed for the CrewAI setup"""
    
    # Initialize LLM
    basic_llm = LLM(model=llm_model, temperature=temperature)
    
    # Create Search Queries Recommendation Agent
    search_queries_recommendation_agent = Agent(
        role="Search Queries Recommendation Agent",
        goal="\n".join([
                "To provide a list of suggested search queries to be passed to the search engine.",
                "The queries must be varied and looking for specific items."
            ]),
        backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
        llm=basic_llm,
        verbose=True,
    )
    
    # Create Search Engine Agent
    search_engine_agent = Agent(
        role="Search Engine Agent",
        goal="To search for products based on the suggested search query",
        backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
        llm=basic_llm,
        verbose=True,
        tools=[search_engine_tool]
    )
    
    # Create Scraping Agent
    scraping_agent = Agent(
        role="Web scraping agent",
        goal="To extract details from any website",
        backstory="The agent is designed to help in looking for required values from any website url. These details will be used to decide which best product to buy.",
        llm=basic_llm,
        tools=[web_scraping_tool],
        verbose=True,
    )
    
    # Create Procurement Report Author Agent
    procurement_report_author_agent = Agent(
        role="Procurement Report Author Agent",
        goal="To generate a professional HTML page for the procurement report",
        backstory="The agent is designed to assist in generating a professional HTML page for the procurement report after looking into a list of products.",
        llm=basic_llm,
        verbose=True,
    )
    
    return {
        "search_queries_recommendation_agent": search_queries_recommendation_agent,
        "search_engine_agent": search_engine_agent,
        "scraping_agent": scraping_agent,
        "procurement_report_author_agent": procurement_report_author_agent
    } 