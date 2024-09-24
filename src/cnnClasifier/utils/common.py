import os
from box.exceptions import BoxValueError
import yaml
from cnnClasifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and returns
    
    Args:
        path_to_yaml: Path like input
    
    Raises:
        valueError: If yaml file is empty
        e: empty file
    
    Returns:
        configBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """"Create list of directories

    Args:
        path_to_directories (list): List of path of directories
        ignore_log (bool, optional):  ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created Director at: {path} ")


@ensure_annotations
def save_json(path:Path, data: dict):
    """save json data
    
    Args:
        path (Path): Path to json file
        data (dict): Data to be saved in json file
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ save binary data
    
    Args:
        data (Any): Data to be saved in binary file
        path (Path): Path to binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    
    Args:
        path (Path): Path to binary file

    Returns:
        Any: object stored in the file
    """
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): Path to file
    
    Returns:
        str: Size of file in KB
    """
    size_in_kb = round(os.path.getatime(path) / 1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())