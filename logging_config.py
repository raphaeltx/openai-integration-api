# logging_config.py
import logging

# Configure the logger
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s]: %(message)s'
    )

# Call setup_logging to configure logging
setup_logging()

# Get the logger
logger = logging.getLogger(__name__)