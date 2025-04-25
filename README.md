# CrewAI Procurement Agent

This project demonstrates the use of CrewAI to create an AI-powered procurement agent that helps find, compare, and recommend products for purchase. It uses a team of specialized AI agents to search for products, scrape product information, and generate procurement reports.

## Features

- **Search Query Generation**: Creates targeted search queries for finding specific products
- **Web Search**: Performs searches using the Tavily search API
- **Product Scraping**: Extracts detailed product information from e-commerce websites
- **Report Generation**: Creates professional HTML procurement reports with recommendations

## Project Structure

```
crewai_procurement_agent/
├── ai-agent-output/            # Directory for output files
├── src/                        # Source code
│   ├── __init__.py
│   ├── agents.py               # Agent definitions
│   ├── crew.py                 # CrewAI crew setup
│   ├── models.py               # Pydantic data models
│   ├── tasks.py                # Task definitions
│   └── tools.py                # Custom tools
├── .gitignore                  # Git ignore file
├── env.example                 # Example environment variables
├── main.py                     # Main execution script
├── README.md                   # Project documentation
└── requirements.txt            # Dependencies
```

## Prerequisites

- Python 3.8+
- API keys for:
  - OpenAI
  - AgentOps
  - Tavily
  - ScrapegraphAI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crewai-procurement-agent.git
   cd crewai-procurement-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp env.example .env
   ```
   Then edit the `.env` file and add your API keys.

## Usage

Run the main script:

```bash
python main.py
```

The script will:
1. Generate search queries for products
2. Search for products using these queries
3. Scrape detailed information from product pages
4. Generate a procurement report with recommendations

Results will be saved in the `ai-agent-output` directory.

## Customization

You can modify the search parameters in `main.py`:

```python
result = crew.kickoff(
    inputs={
        "product_name": "coffee machine for the office",  # Change to your desired product
        "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],  # Target websites
        "country_name": "Egypt",  # Target country
        "no_keywords": 10,  # Number of search keywords to generate
        "language": "English",  # Search language
        "score_th": 0.10,  # Minimum confidence score for search results
        "top_recommendations_no": 10  # Number of top products to recommend
    }
)
```

## License

MIT

## Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [AgentOps](https://www.agentops.ai/)
- [Tavily](https://tavily.com/)
- [ScrapegraphAI](https://www.scrapegraph.ai/)

## Output Files

The CrewAI ProcureBot generates several output files during its procurement process:

1. **step_1_suggested_search_queries.json**: Contains the AI-generated search queries for finding the requested product across specified e-commerce websites.

2. **step_2_search_results.json**: Stores the raw search results from the web search, including titles, URLs, content snippets, and relevance scores.

3. **step_3_search_results.json**: Contains detailed product information extracted from the search results, including prices, specifications, images, and AI-generated recommendation rankings.

4. **step_4_procurement_report.html**: A professional HTML report summarizing the procurement findings, including product comparisons, pricing analysis, and purchasing recommendations.

Click [here](ai-agent-output\step_4_procurement_report.html) to view the final output

These files document the step-by-step process of the procurement workflow and provide valuable insights for making informed purchasing decisions. 

