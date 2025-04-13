import configparser
import os

class ConfigReader:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)
            cls._config = configparser.ConfigParser()
            config_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.ini')
            print(f"Config file path (inside ConfigReader): {config_file_path}")

            if not os.path.exists(config_file_path):
                print(f"Error: Config file NOT FOUND at {config_file_path}")
                return None  # Or raise an exception

            try:
                with open(config_file_path, 'r') as f:
                    content = f.read()
                    print("Config file content (inside ConfigReader):\n--- START ---\n", content, "\n--- END ---")
                cls._config.read(config_file_path)
            except configparser.MissingSectionHeaderError as e:
                print(f"Error loading config file (inside ConfigReader): {e}")
                cls._config = None
            except Exception as e:
                print(f"An unexpected error occurred while reading config: {e}")
                cls._config = None
        return cls._instance

    def get(self, section, key):
        if self._config:
            try:
                return self._config.get(section, key)
            except (configparser.NoSectionError, configparser.NoOptionError):
                return None
        else:
            print("Warning: ConfigParser object is not initialized.")
            return None