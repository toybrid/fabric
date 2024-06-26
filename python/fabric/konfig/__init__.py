import os
import json
from pathlib import Path
from dataclasses import dataclass
from fabric import utils
from fabric.konfig.loaders import JsonLoader


def merge_dicts(dicts):
    """
    Merges a list of dictionaries into a single dictionary.

    Parameters:
    dicts (list): A list of dictionaries to be merged.

    Returns:
    dict: A single dictionary that is the result of merging all input dictionaries.
    """

    def merge_two_dicts(dict1, dict2):
        """
        Merges two dictionaries recursively.

        Parameters:
        dict1 (dict): The first dictionary to merge.
        dict2 (dict): The second dictionary to merge.

        Returns:
        dict: A new dictionary that is the result of merging dict1 and dict2.

        The function merges dictionaries in a way that if a key is present in both dictionaries,
        and the corresponding values are also dictionaries, the function recursively merges them.
        If a key is present in only one dictionary, the corresponding value is used as is.
        """

        merged = dict1.copy()
        for key, value in dict2.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = merge_two_dicts(merged[key], value)
            else:
                merged[key] = value
        return merged

    result = {}
    for item in dicts:
        result = merge_two_dicts(result, item)

    return result

@dataclass
class KonfigSettings:
    resolve_tree: dict
    release_path: str


class KonfigEntity:
    """
    A class to represent a configuration entity.

    Attributes:
    None

    Methods:
    __init__(self, **entries):
        Initializes a new KonfigEntity instance.

        Parameters:
        entries (dict): A dictionary of key-value pairs representing the configuration attributes.
                        If a value is a dictionary, it will be recursively converted into a KonfigEntity instance.

    __repr__(self):
        Returns a string representation of the KonfigEntity instance.
    """

    def __init__(self, **entries):
        """
        Initializes a new KonfigEntity instance.

        Parameters:
        entries (dict): A dictionary of key-value pairs representing the configuration attributes.
                        If a value is a dictionary, it will be recursively converted into a KonfigEntity instance.
        """
        for key, value in entries.items():
            if isinstance(value, dict):
                value = KonfigEntity(**value)
            setattr(self, key, value)

    def __repr__(self):
        """
        Returns a string representation of the KonfigEntity instance.

        Returns:
        str: A string representation of the KonfigEntity instance.
        """
        return f"{self.__dict__}"
    
    def __repr__(self):
        return f"{self.__dict__}"
    
class KonfigAPI:
    """
    KonfigAPI is a class that provides methods to load and resolve configuration data.

    Attributes:
    rez_package_name (str): The name of the Rez package.
    config_file_name (str): The name of the configuration file.
    loader (JsonLoader): The loader object used to load configuration data.

    Methods:
    _get_konfig_settings():
        Private method to load and parse the konfig settings from the package's 'konfig.json' file.

    get_repo_config():
        Method to load and parse the repository specific configuration data.

    resolve():
        Method to resolve the configuration data by merging the repository specific configuration 
        with the konfig settings and any additional configuration files found in the resolve tree.
    """

    def __init__(self, rez_package_name, config_file_name, loader=JsonLoader()):
        """
        Initializes a new KonfigAPI instance.

        Parameters:
        rez_package_name (str): The name of the Rez package.
        config_file_name (str): The name of the configuration file.
        loader (JsonLoader, optional): The loader object used to load configuration data. Defaults to JsonLoader().
        """
        self.loader = loader
        self.rez_package_name = rez_package_name
        self.config_file_name = config_file_name

    def _get_konfig_settings(self):
        """
        Private method to load and parse the konfig settings from the package's 'konfig.json' file.

        Returns:
        KonfigSettings: An instance of KonfigSettings containing the parsed settings.
        """
        package_root = Path(utils.get_rez_package_root(self.rez_package_name))
        settings_file = package_root.joinpath('configs', 'konfig.json')
        with open(settings_file, 'r') as fl:
            return KonfigSettings(**json.load(fl))
        return None

    def get_repo_config(self):
        """
        Method to load and parse the repository specific configuration data.

        Returns:
        dict: A dictionary containing the parsed configuration data.
        """
        package_root = utils.get_rez_package_root(self.rez_package_name)
        config_file_path = package_root.joinpath('configs',f'{self.config_file_name}.{self.loader.extension}')
        with open(config_file_path, 'r') as fl:
            data = json.load(fl)
            return data

    def resolve(self):
        """
        Method to resolve the configuration data by merging the repository specific configuration 
        with the konfig settings and any additional configuration files found in the resolve tree.

        Returns:
        KonfigEntity: An instance of KonfigEntity containing the resolved configuration data.
        """
        config_data = [self.get_repo_config()]
        konfig_settings = self._get_konfig_settings()
        for path_item in konfig_settings.resolve_tree:
             base_path = Path(os.path.expandvars(path_item))
             config_file_path = base_path.joinpath(
                                                self.rez_package_name,
                                                f'{self.config_file_name}.{self.loader.extension}'
                                                ).expanduser()
             if config_file_path.exists():
                config_data.append(self.loader.load(config_file_path))

        merged_config = merge_dicts(config_data)
        return KonfigEntity(**merged_config)