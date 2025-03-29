"""
Basic example of using DeepResearch.
"""

from deepresearch import ResearchAgent
from deepresearch.tools import SearchTool
from deepresearch.utils.logger import setup_logging

def main():
    """Run a basic research example."""
    # Set up logging
    setup_logging()
    
    # Initialize the research agent
    agent = ResearchAgent()
    
    # Add search tool
    search_tool = SearchTool()
    agent.add_tool(search_tool)
    
    # Conduct research
    query = "What are the latest developments in quantum computing?"
    results = agent.research(query)
    
    # Print results
    print("\nResearch Results:")
    print("-" * 50)
    print(f"Query: {query}")
    print("\nFindings:")
    for result in results.get("results", []):
        print(f"- {result}")

if __name__ == "__main__":
    main() 