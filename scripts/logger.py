from loguru import logger
from scripts.config import LOG_DIR

# Remove default logger
logger.remove()

# Log to console
logger.add(
    sink=lambda message: print(message, end=""),
    level="INFO",
)

# Log to file
logger.add(
    LOG_DIR / "pipeline.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
)

logger.info("Logger initialized successfully.")