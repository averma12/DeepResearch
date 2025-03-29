"""
Research flow orchestration.
"""

from typing import Any, Dict, Optional

from ..agents.base import BaseAgent

class ResearchFlow:
    """Manages the research process flow."""
    
    def __init__(self, agent: BaseAgent):
        """
        Initialize the research flow.
        
        Args:
            agent: The research agent to use
        """
        self.agent = agent
    
    def execute(self, query: str) -> Dict[str, Any]:
        """
        Execute a research query.
        
        Args:
            query: The research query to investigate
            
        Returns:
            Research results
        """
        # Pre-processing phase
        self._validate_query(query)
        
        # Main research phase
        results = self.agent.research(query)
        
        # Post-processing phase
        self._validate_results(results)
        
        return results
    
    def _validate_query(self, query: str) -> None:
        """
        Validate the research query.
        
        Args:
            query: The query to validate
            
        Raises:
            ValueError: If the query is invalid
        """
        if not query or not query.strip():
            raise ValueError("Query cannot be empty")
    
    def _validate_results(self, results: Dict[str, Any]) -> None:
        """
        Validate the research results.
        
        Args:
            results: The results to validate
            
        Raises:
            ValueError: If the results are invalid
        """
        if not results:
            raise ValueError("Research results cannot be empty") 