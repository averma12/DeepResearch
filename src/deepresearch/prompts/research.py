"""
System prompts for research operations.
"""

RESEARCH_SYSTEM_PROMPT = """You are an AI research assistant. Your task is to help users conduct thorough research on various topics.
Follow these guidelines:
1. Be thorough and systematic in your research
2. Cite sources when possible
3. Organize information clearly
4. Maintain objectivity
5. Consider multiple perspectives
"""

ANALYSIS_PROMPT = """Analyze the following information and provide a structured summary:
{content}

Focus on:
1. Key findings
2. Supporting evidence
3. Potential implications
4. Areas for further research
"""

SUMMARY_PROMPT = """Create a concise summary of the research findings:
{content}

Include:
1. Main points
2. Key conclusions
3. Recommendations
4. Sources used
""" 