import os
import agentops
from dotenv import load_dotenv
from src.agents import create_agents
from src.tasks import create_tasks
from src.crew import create_crew
from src.tools import init_tools

def main():
    # Load environment variables
    load_dotenv()
    
    # Check for required environment variables
    required_vars = [
        "OPENAI_API_KEY", 
        "AGENTOPS_API_KEY", 
        "TAVILY_API_KEY", 
        "SCRAPEGRAPH_API_KEY"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        print(f"Error: Missing environment variables: {', '.join(missing_vars)}")
        print("Create a .env file with these variables. See .env.example for reference.")
        return
    
    # Set environment variables
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    
    # Initialize AgentOps
    agentops.init(
        api_key=os.getenv("AGENTOPS_API_KEY"),
        skip_auto_end_session=True,
        default_tags=['crewai']
    )
    
    # Initialize tools
    init_tools(
        tavily_api_key=os.getenv("TAVILY_API_KEY"),
        scrapegraph_api_key=os.getenv("SCRAPEGRAPH_API_KEY")
    )
    
    # Create output directory
    output_dir = "./ai-agent-output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Setup agents, tasks, and crew
    agents = create_agents(llm_model="gpt-4o", temperature=0)
    tasks = create_tasks(agents, output_dir=output_dir)
    crew = create_crew(agents, tasks)
    
    print("Starting crew execution...")
    
    # Run the crew
    result = crew.kickoff(
        inputs={
            "product_name": "coffee machine for the office",
            "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
            "country_name": "Egypt",
            "no_keywords": 10,
            "language": "English",
            "score_th": 0.10,
            "top_recommendations_no": 10
        }
    )
    
    print("Crew execution completed!")
    print(f"Results are saved in {output_dir}")
    
    return result

if __name__ == "__main__":
    main() 