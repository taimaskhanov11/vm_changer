import binascii
import os
import random
import re
import string
from pathlib import Path

from vm_changer.config.config import DownloadedVm, SAVED_VM_PATH, RANDOM_VM_NAME_LOWERCASE_ONLY, RANDOM_VM_NAME_LENGTH

letters = string.ascii_lowercase if RANDOM_VM_NAME_LOWERCASE_ONLY else string.ascii_letters


def save_vm(filename, data):
    with open(Path(SAVED_VM_PATH, f"{filename}.vmx"), "w", encoding="utf-8") as f:
        f.write(data)


def find_field(field_name: str):
    field = re.findall(f"{field_name} .*", DownloadedVm.data)[0]
    return field


def get_even_integer():
    while True:
        x = os.urandom(1)
        p = binascii.hexlify(x)
        int_pre = int(p, 16)
        if int_pre == 0:
            return p.decode().upper()
        elif int_pre % 2 == 0:
            return p.decode().upper()


def get_random_vm_name():
    return ''.join(random.choices(letters, k=RANDOM_VM_NAME_LENGTH))
