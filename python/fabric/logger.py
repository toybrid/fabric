import os
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from fabric import studio, infra


def get_log_file(app_name):
    """
    This function generates a log file path based on the given application name.

    Parameters:
    app_name (str): The name of the application for which the log file is being generated.

    Returns: str
    """
    log_base = studio.get_log_base()
    log_file = log_base.joinpath(infra.get_user(), app_name, f'{app_name}.log')
    log_file.parent.mkdir(parents=True, exist_ok=True)
    return log_file.as_posix()

def get_level_from_env():
    """
    This function retrieves the log level from the environment variable 'TB_LOG_LEVEL'.
    If the variable is not set, it defaults to 'INFO'. The function then converts
    the string log level to the corresponding logging module log level.

    Returns: int
    """
    level = os.environ.get('TB_LOG_LEVEL', 'INFO')
    if level == 'DEBUG':
        return logging.DEBUG
    elif level == 'INFO':
        return logging.INFO
    elif level == 'WARNING':
        return logging.WARNING
    elif level == 'ERROR':
        return logging.ERROR
    elif level == 'CRITICAL':
        return logging.CRITICAL
    else:
        return logging.DEBUG

def get_debug_str():
    """
    This function generates a debug string format based on the log level set in the environment 
    variable 'TB_LOG_LEVEL'. If the variable is not set or its value is not recognized, it defaults 
    to 'INFO' level.

    Returns: str
    """
    level = os.environ.get('TB_LOG_LEVEL', 'INFO')
    if level == 'DEBUG':
        return '%(asctime)s - %(lineno)d - %(process)d - %(pathname)s - %(funcName)s - %(levelname)s - %(message)s'
    else:
        return '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s'
                      
class FabricLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        """
        Initialize a new instance of FabricLogger.

        Parameters:
        name (str): The name of the logger.
        level (int, optional): The log level for the logger. Defaults to logging.NOTSET.

        Returns: None

        Example:
        >> import logging
        >> from fabric.logger import FabricLogger
        >> logging.setLoggerClass(FabricLogger)
        >> log = logging.getLogger('too_name')
        """
        super().__init__(name, level)

        self.setLevel(get_level_from_env())

        console_handler = logging.StreamHandler()
        console_handler.setLevel(get_level_from_env())

        self.log_file_path = get_log_file(name)

        file_handler = TimedRotatingFileHandler(self.log_file_path, when='midnight', interval=1, backupCount=7)
        file_handler.setLevel(get_level_from_env())

        formatter = logging.Formatter(get_debug_str())
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.addHandler(console_handler)
        self.addHandler(file_handler)
