"""
Basic tests for the DeepResearch package.
"""

import pytest

from deepresearch.core.memory import ResearchMemory
from deepresearch.core.flow import ResearchFlow
from deepresearch.agents.base import BaseAgent

class TestAgent(BaseAgent):
    """Test agent implementation."""
    
    def research(self, query: str):
        return {"query": query, "results": ["Test result"]}

def test_research_memory():
    """Test research memory functionality."""
    memory = ResearchMemory()
    
    # Test adding facts
    memory.add_fact({"fact": "Test fact"})
    assert len(memory.get_facts()) == 1
    
    # Test adding sources
    memory.add_source("Test source")
    assert len(memory.get_sources()) == 1
    
    # Test context
    memory.update_context("test_key", "test_value")
    assert memory.get_context("test_key") == "test_value"

def test_research_flow():
    """Test research flow functionality."""
    agent = TestAgent()
    flow = ResearchFlow(agent)
    
    # Test valid query
    results = flow.execute("Test query")
    assert results["query"] == "Test query"
    
    # Test invalid query
    with pytest.raises(ValueError):
        flow.execute("") 