import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Log file naming with timestamp
LOG_FILENAME = os.path.join(LOG_DIR, f"automation_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

def setup_logging(log_level=logging.INFO):
    """
    Centralized logging configuration for the automation framework

    Args:
        log_level: Logging level (default: logging.INFO)
    """
    # Create logger
    logger = logging.getLogger('automation_framework')
    logger.setLevel(log_level)

    # Remove existing handlers to avoid duplicates
    logger.handlers = []

    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )

    # File handler
    file_handler = logging.FileHandler(LOG_FILENAME)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def get_logger(module_name):
    """
    Get or create a logger instance for a specific module

    Args:
        module_name: Name of the module (typically __name__)

    Returns:
        Logger instance
    """
    return logging.getLogger(f'automation_framework.{module_name}')

