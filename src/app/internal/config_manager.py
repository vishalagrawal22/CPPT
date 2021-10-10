from pathlib import Path

import yaml

from .file_manager import read_from_file

user_config_path = Path.home() / ".config/cppt/config.yaml"


def create_config():
    default_config_path = Path(__file__).parent / "default_config.yaml"
    default_config = open(default_config_path, "r")
    default_data = yaml.safe_load(default_config)

    user_config_path.parent.mkdir(parents=True, exist_ok=True)
    user_config = open(user_config_path, "w")

    yaml.dump(default_data, user_config, default_flow_style=False)


def get_config_path():
    return user_config_path.resolve()
