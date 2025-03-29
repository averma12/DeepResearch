"""
Research agent implementation.
"""

from typing import Any, Dict, List

from .base import BaseAgent
from ..core.memory import ResearchMemory
from ..prompts.research import RESEARCH_SYSTEM_PROMPT

class ResearchAgent(BaseAgent):
    """Agent for conducting research."""
    
    def __init__(self, memory: ResearchMemory = None):
        """
        Initialize the research agent.
        
        Args:
            memory: Optional research memory instance
        """
        super().__init__(memory)
        self.system_prompt = RESEARCH_SYSTEM_PROMPT
    
    def research(self, query: str) -> Dict[str, Any]:
        """
        Conduct research on the given query.
        
        Args:
            query: The research query
            
        Returns:
            Research results
        """
        # Initialize results
        results = {
            "query": query,
            "results": [],
            "sources": []
        }
        
        # Use search tool if available
        search_tool = self.get_tool("search")
        if search_tool:
            search_results = search_tool.execute(query=query)
            results["results"].extend(search_results.get("results", []))
            
            # Add sources to memory
            for result in search_results.get("results", []):
                if "url" in result:
                    self.memory.add_source(result["url"])
        
        # Add facts to memory
        for result in results["results"]:
            if "content" in result:
                self.memory.add_fact({"content": result["content"]})
        
        return results 