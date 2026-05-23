import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("intent-engine")

def log_event(data):
  logger.info(data)