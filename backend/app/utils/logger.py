import logging
import sys
import os
from datetime import datetime

# 1. Setup log directory
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 2. Create a unique filename for each session (optional) or use a fixed one
LOG_FILE = os.path.join(LOG_DIR, f"biodetect_{datetime.now().strftime('%Y-%m-%d')}.log")

def setup_logger():
    """Configures the global logging settings."""
    
    # Create logger
    logger = logging.getLogger("BioDetectAI")
    logger.setLevel(logging.INFO)

    # Formatter: [Time] [Level] [Module] -> Message
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(module)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console Handler (Prints logs to your terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # File Handler (Saves logs to the logs/ folder)
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

# Initialize the logger instance
logger = setup_logger()