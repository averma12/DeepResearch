"""
Logging utility setup.
"""

import logging
import sys
from typing import Optional

def setup_logging(
    level: int = logging.INFO,
    format_string: Optional[str] = None,
    output_file: Optional[str] = None
) -> None:
    """
    Set up logging configuration.
    
    Args:
        level: Logging level
        format_string: Custom format string
        output_file: Optional file to write logs to
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(format_string))
    handlers.append(console_handler)
    
    # File handler if specified
    if output_file:
        file_handler = logging.FileHandler(output_file)
        file_handler.setFormatter(logging.Formatter(format_string))
        handlers.append(file_handler)
    
    # Configure root logger
    logging.basicConfig(
        level=level,
        handlers=handlers,
        force=True
    ) 