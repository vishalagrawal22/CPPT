from pathlib import Path

import yaml

from .file_manager import read_from_file

config_path = Path.home() / ".config/cppt/config.yaml"


def create_config():
    config_path.parent.mkdir(parents=True, exist_ok=True)
    default_config_path = Path(__file__).parent / "default_config.yaml"
    config_path.write_bytes(default_config_path.read_bytes())


def get_config_path():
    return config_path.resolve()
