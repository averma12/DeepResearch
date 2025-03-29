"""
Base agent class for research operations.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..core.memory import ResearchMemory
from ..tools.base import BaseTool

class BaseAgent(ABC):
    """Base class for all research agents."""
    
    def __init__(self, memory: Optional[ResearchMemory] = None):
        """
        Initialize the agent.
        
        Args:
            memory: Optional research memory instance
        """
        self.memory = memory or ResearchMemory()
        self.tools: List[BaseTool] = []
    
    @abstractmethod
    def research(self, query: str) -> Dict[str, Any]:
        """
        Conduct research on the given query.
        
        Args:
            query: The research query
            
        Returns:
            Research results
        """
        pass
    
    def add_tool(self, tool: BaseTool) -> None:
        """
        Add a tool to the agent's toolkit.
        
        Args:
            tool: The tool to add
        """
        self.tools.append(tool)
    
    def get_tool(self, name: str) -> Optional[BaseTool]:
        """
        Get a tool by name.
        
        Args:
            name: The name of the tool
            
        Returns:
            The tool if found, None otherwise
        """
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None 