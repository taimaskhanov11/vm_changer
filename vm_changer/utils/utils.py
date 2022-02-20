import re
from pathlib import Path

from vm_changer.config.config import DownloadedVm, SAVED_VM_PATH


def save_vm(filename,data):
    with open(Path(SAVED_VM_PATH, f"{filename}.vmx"), "w", encoding="utf-8") as f:
        f.write(data)


def find_field(field_name: str):
    field = re.findall(f"{field_name} .*", DownloadedVm.data)[0]
    return field


