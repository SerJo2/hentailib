import logging

from .config import Confing
def base_logger(name, log_file, level=logging.INFO):
    """Sets up a logger with the specified name, file, and level."""

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        # Создаем обработчик для файла
        handler = logging.FileHandler(log_file, encoding='utf-8')
        handler.setLevel(level)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
    return logger
