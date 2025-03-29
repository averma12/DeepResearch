"""
Research memory implementation for maintaining state.
"""

from typing import Any, Dict, List, Optional

class ResearchMemory:
    """Maintains research state and history."""
    
    def __init__(self):
        """Initialize the research memory."""
        self.facts: List[Dict[str, Any]] = []
        self.sources: List[str] = []
        self.context: Dict[str, Any] = {}
    
    def add_fact(self, fact: Dict[str, Any]) -> None:
        """
        Add a new fact to the memory.
        
        Args:
            fact: The fact to add
        """
        self.facts.append(fact)
    
    def add_source(self, source: str) -> None:
        """
        Add a new source to the memory.
        
        Args:
            source: The source to add
        """
        self.sources.append(source)
    
    def update_context(self, key: str, value: Any) -> None:
        """
        Update the research context.
        
        Args:
            key: The context key
            value: The context value
        """
        self.context[key] = value
    
    def get_facts(self) -> List[Dict[str, Any]]:
        """
        Get all stored facts.
        
        Returns:
            List of facts
        """
        return self.facts
    
    def get_sources(self) -> List[str]:
        """
        Get all stored sources.
        
        Returns:
            List of sources
        """
        return self.sources
    
    def get_context(self, key: Optional[str] = None) -> Any:
        """
        Get context value(s).
        
        Args:
            key: Optional specific context key
            
        Returns:
            Context value(s)
        """
        if key is not None:
            return self.context.get(key)
        return self.context 