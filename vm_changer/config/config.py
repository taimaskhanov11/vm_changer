from pathlib import Path

import yaml


def get_config_data(path: str | Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_data_list(path) -> list[str]:
    arr = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                arr.append(line)
    return arr


def get_vm_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


CONFIG = get_config_data("../config.yaml")
# CREATED_VM_PATH = CONFIG["created_vm"]
CREATED_VM_NAME = CONFIG["created_vm_name"]
DOWNLOADED_VM_PATH = CONFIG["downloaded_vm"]
SAVED_VM_PATH = CONFIG["saved_vm"]
PROCESSORS = get_data_list("../Processors.txt")
SSD = get_data_list("../SSD.txt")
WINDOWS_PATH = CONFIG["windows_path"]
ITER_COUNT = CONFIG["iter_count"]


class DownloadedVm:
    """DOWNLOADED_VM"""
    data: str = get_vm_data(DOWNLOADED_VM_PATH)

    @classmethod
    def replace_vm(cls, old: str, new: str):
        cls.data = cls.data.replace(old, new)
