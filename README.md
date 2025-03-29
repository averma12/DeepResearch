# DeepResearch

An AI-powered research assistant that helps you conduct deep research on any topic using advanced language models and specialized tools.

## Features

- Intelligent research flow orchestration
- Stateful research memory
- Modular agent system
- Extensible tool framework
- Configurable prompts

## Installation

```bash
pip install deepresearch
```

## Quick Start

```python
from deepresearch import ResearchAgent

# Initialize the research agent
agent = ResearchAgent()

# Start a research session
results = agent.research("What are the latest developments in quantum computing?")
```

## Project Structure

```
deepresearch/
├── src/                     # Source code directory
│   └── deepresearch/        # Main package
│       ├── agents/          # Agent implementations
│       ├── core/            # Core functionality
│       ├── prompts/         # System prompts
│       ├── tools/           # Tool implementations
│       ├── utils/           # Utility functions
│       └── config/          # Configuration
├── tests/                   # Test directory
└── examples/                # Example scripts
```

## Development

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
3. Run tests:
   ```bash
   pytest
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.