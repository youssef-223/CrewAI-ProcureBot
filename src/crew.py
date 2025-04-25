from crewai import Crew, Process
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
import agentops

def create_crew(agents, tasks, company_info="Rankyx is a company that provides AI solutions to help websites refine their search and recommendation systems."):
    """Create the CrewAI crew with the given agents and tasks"""
    
    # Create a knowledge source with company information
    company_context = StringKnowledgeSource(
        content=company_info
    )
    
    # Create the crew
    crew = Crew(
        agents=[
            agents["search_queries_recommendation_agent"],
            agents["search_engine_agent"],
            agents["scraping_agent"],
            agents["procurement_report_author_agent"],
        ],
        tasks=[
            tasks["search_queries_recommendation_task"],
            tasks["search_engine_task"],
            tasks["scraping_task"],
            tasks["procurement_report_author_task"],
        ],
        process=Process.sequential,
        knowledge_sources=[company_context]
    )
    
    return crew 