import json
import os
from dotenv import load_dotenv

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        load_dotenv()  # Load environment variables from .env file

        base_config_path = os.path.join(self.get_project_root(), "utils", "config.json")
        self._config_data = self._load_json_file(base_config_path, "base configuration")

        app_env = os.getenv("APP_ENV")
        if app_env:
            env_config_filename = f"config.{app_env}.json"
            env_config_path = os.path.join(self.get_project_root(), "utils", env_config_filename)
            env_config = self._load_json_file(
                env_config_path,
                f"environment-specific configuration for '{app_env}'"
            )
            if env_config:
                self._config_data = self._deep_merge(self._config_data, env_config)

    def _load_json_file(self, file_path, description):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"Warning: {description.capitalize()} file not found at {file_path}. Using empty configuration.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Error decoding JSON from {file_path}. Using empty configuration.")
            return {}
        except Exception as e:
            print(f"Error: An unexpected error occurred while loading {description} from {file_path}: {e}. Using empty configuration.")
            return {}

    def _deep_merge(self, base_dict, merge_dict):
        for key, value in merge_dict.items():
            if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
                base_dict[key] = self._deep_merge(base_dict[key], value)
            else:
                base_dict[key] = value
        return base_dict

    def get(self, key, default=None):
        # Prioritize environment variables for sensitive info
        if key == "app_settings.username":
            return os.getenv("QMS_USERNAME", self._config_data.get("app_settings", {}).get("username", default))
        if key == "app_settings.password":
            return os.getenv("QMS_PASSWORD", self._config_data.get("app_settings", {}).get("password", default))

        keys = key.split('.')
        val = self._config_data
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                if default is not None:
                    return default
                raise KeyError(f"Configuration key '{key}' not found.")
        return val

    # ✅ NEW: BASE URL SUPPORT (FROM .env OR JSON)
    def get_base_url(self):
        return os.getenv("BASE_URL") or self.get("app_settings.base_url")

    @staticmethod
    def get_project_root():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Initialize the config instance
config = Config()
