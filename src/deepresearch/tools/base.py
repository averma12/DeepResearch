"""
Base tool class for all research tools.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTool(ABC):
    """Base class for all research tools."""
    
    def __init__(self, name: str):
        """
        Initialize the tool.
        
        Args:
            name: The name of the tool
        """
        self.name = name
    
    @abstractmethod
    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Execute the tool.
        
        Args:
            **kwargs: Tool arguments
            
        Returns:
            Tool execution results
        """
        pass 