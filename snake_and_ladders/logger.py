import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logger.log"),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)

    return logger

logger = setup_logging()
