from pathlib import Path
import yaml
import xarray as xr
import pandas as pd

# Absolute path to project root (pcic-climate-extract/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _resolve_path(relative_path):
    """
    Resolve a path relative to the project root.
    """
    path = PROJECT_ROOT / relative_path
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path

def resolve_relative_path(relative_path):
    """
    Resolve a config-relative path to an absolute path under the project root.
    """
    return _resolve_path(relative_path)

def load_yaml(relative_path):
    """
    Load a YAML file relative to the project root.
    """
    path = _resolve_path(relative_path)
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_pcic_netcdf(relative_path):
    """
    Load a PCIC-Blend netCDF dataset.
    """
    path = _resolve_path(relative_path)
    return xr.open_dataset(path, decode_times=False)


def load_station_csv(relative_path):
    """
    Load a station CSV file.
    """
    path = _resolve_path(relative_path)
    return pd.read_csv(path)
