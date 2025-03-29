"""
Main entry point for the DeepResearch application.
"""

import logging
from typing import Optional

from .agents import ResearchAgent
from .core import ResearchFlow
from .utils.logger import setup_logging

logger = logging.getLogger(__name__)

def main(query: str, output_file: Optional[str] = None) -> None:
    """
    Main entry point for running research queries.
    
    Args:
        query: The research query to investigate
        output_file: Optional file path to save results
    """
    setup_logging()
    logger.info(f"Starting research for query: {query}")
    
    agent = ResearchAgent()
    flow = ResearchFlow(agent)
    
    results = flow.execute(query)
    
    if output_file:
        with open(output_file, "w") as f:
            f.write(str(results))
        logger.info(f"Results saved to {output_file}")
    else:
        print(results)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m deepresearch.main 'your research query' [output_file]")
        sys.exit(1)
    
    query = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    main(query, output_file) 