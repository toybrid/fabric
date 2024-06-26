import json
from abc import ABC, abstractmethod
from pathlib import Path

class LoaderBase(ABC):
    """
    Abstract base class for loading data from files.

    This class defines an abstract method `load` that subclasses must implement to load data from a file.
    """

    @abstractmethod
    def load(self, path: Path):
        """
        Load data from a file at the specified path.

        This method is intended to be implemented by subclasses, as it is an abstract method.
        The subclass should define its own implementation to load data from the specified file.

        Parameters:
        path (Path): The path to the file from which to load data.

        Returns:
        dict: The loaded data. The type of the returned data depends on the specific implementation of the subclass.

        Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        PermissionError: If the file at the specified path cannot be accessed due to insufficient permissions.
        IOError: If an error occurs while reading the file.
        """
        pass

    @property
    @abstractmethod
    def extension(self):
        pass


class JsonLoader(LoaderBase):
    """
    Class for loading data from JSON files.

    This class extends the LoaderBase abstract base class and implements the load 
    method to load data from a JSON file.
    """
    def load(self, path: Path):
        """
        Load data from a JSON file at the specified path.

        Parameters:
        path (Path): The path to the JSON file from which to load data.

        Returns: dict

        Raises:
        FileNotFoundError: If the file at the specified path does not exist or not a file.
        """
        if not path.is_file():
            raise FileNotFoundError(f'File not found: {path}')
        
        if not path.exists():
            raise FileNotFoundError(f'File does not exist: {path}')

        with open(path, 'r') as file:
            data = json.load(file)
        return data
    
    @property
    def extension(self):
        return 'json'