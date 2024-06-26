import os
from pathlib import Path

def get_rez_package_root(package_name):
    """
    This function retrieves the root directory of a Rez package.

    Parameters:
    package_name (str): The name of the Rez package.

    Returns: str
    """
    package_root = Path(os.getenv(f'REZ_{package_name.upper()}_ROOT', None))
    if package_root.exists():
        return package_root
    else:
        raise FileNotFoundError(f'Could not find Rez package root {package_root.as_posix()}')
