# clinical_playwright_project/utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler
from utils.config import config # Import the config object

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project/clinical_playwright_project
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "test.log")

def get_logger(name: str = "automation"):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    # Get log level from config, default to INFO
    log_level_str = config.get("log_level", "INFO").upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger.setLevel(log_level)

    # Rotating file handler (10MB per file, keep 3 backups)
    fh = RotatingFileHandler(LOG_FILE, maxBytes=10*1024*1024, backupCount=3)
    fh.setLevel(logging.DEBUG) # File always logs DEBUG

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(log_level) # Console logs at configured level

    formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(name)s — %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    # avoid duplicate logs on repeated imports
    logger.propagate = False
    return logger
