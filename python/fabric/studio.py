import os
from pathlib import Path

def get_software_base():
    """
    This function retrieves the base directory for software.

    It checks the environment variable 'TB_SOFTWARE_BASE_DIR' for the base directory path.
    If the path exists, it returns the Path object.
    If the path does not exist, it raises an IOError with a descriptive error message.

    Returns: Path

    Raises: IOError
    """
    base_dir = Path(os.environ.get('TB_SOFTWARE_BASE_DIR', None))
    if base_dir.exists():
        return base_dir
    else:
        raise IOError(f'Could not find software base directory {base_dir.as_posix()}')

def get_projects_base():
    """
    This function retrieves the base directory for projects.

    It checks the environment variable 'TB_PROJECTS_BASE_DIR' for the base directory path.
    If the path exists, it returns the Path object.
    If the path does not exist, it raises an IOError with a descriptive error message.

    Returns: Path

    Raises: IOError
    """
    base_dir = Path(os.environ.get('TB_PROJECTS_BASE_DIR', None))
    if base_dir.exists():
        return base_dir
    else:
        raise IOError(f'Could not find projects base directory {base_dir.as_posix()}')


def get_repository_base():
    """
    This function retrieves the base directory for repositories.

    It checks the environment variable 'TB_REPOSITORY_BASE_DIR' for the base directory path.
    If the path exists, it returns the Path object.
    If the path does not exist, it raises an IOError with a descriptive error message.

    Returns: Path

    Raises: IOError
    """
    base_dir = Path(os.environ.get('TB_REPOSITORY_BASE_DIR', None))
    if base_dir.exists():
        return base_dir
    else:
        raise IOError(f'Could not find repository base directory {base_dir.as_posix()}')

def get_log_base():
    """
    This function retrieves the base directory for logs.

    It checks the environment variable 'TB_LOG_BASE_DIR' for the base directory path.
    If the path exists, it returns the Path object.
    If the path does not exist, it raises an IOError with a descriptive error message.

    Returns: Path

    Raises: IOError
    """
    base_dir = Path(os.environ.get('TB_LOG_BASE_DIR', None))
    if base_dir.exists():
        return base_dir
    else:
        raise IOError(f'Could not find log base directory {base_dir.as_posix()}')
