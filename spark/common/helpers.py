from pathlib import Path
import yaml


def load_config():
    """
    Load the project configuration file.
    """

    config_path = (
        Path(__file__).resolve().parent.parent
        / "config"
        / "config.yaml"
    )

    with open(config_path, "r") as file:
        return yaml.safe_load(file)