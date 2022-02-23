import binascii
import os
import random
import sys

from loguru import logger
from randmac import RandMac

from vm_changer.config.config import CONFIG, DownloadedVm, CREATED_VM_NAME, PROCESSORS, SSD, WINDOWS_PATH, ITER_COUNT, \
    MAC_TYPE
from vm_changer.utils.utils import find_field, save_vm

logger.remove()
logger.add(
    sink=sys.stdout,
    level="TRACE",
    enqueue=True,
    diagnose=True,
    # format="{time}| {message}",
)
logger.add(
    sink=f"../logs/mainlog.log",
    level="TRACE",
    enqueue=True,
    encoding="utf-8",
    diagnose=True,
)

for _ in range(ITER_COUNT):
    logger.warning("\n\nНовая итерация")

    # scsi0:0.fileName
    field_name = "scsi0:0.fileName ="
    field = find_field(field_name)
    new_field = f'{field_name} "{CREATED_VM_NAME}.vmdk"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # displayName
    field_name = "displayName ="
    field = find_field(field_name)
    new_field = f'{field_name} "{CREATED_VM_NAME}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # nvram
    field_name = "nvram ="
    field = find_field(field_name)
    new_field = f'{field_name} "{CREATED_VM_NAME}.nvram"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # sata0:1.fileName
    field_name = "sata0:1.fileName ="
    field = find_field(field_name)
    new_field = f'{field_name} "{CREATED_VM_NAME}.vmdk"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # nvme0:0.fileName
    field_name = "nvme0:0.fileName ="
    field = find_field(field_name)
    new_field = f'{field_name} "{CREATED_VM_NAME}.vmdk"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # extendedConfigFile
    field_name = "extendedConfigFile ="
    field = find_field(field_name)
    new_field = f'{field_name} "{CREATED_VM_NAME}.vmxf"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # scsi0:0.productID
    field_name = "scsi0:0.productID ="
    field = find_field(field_name)
    random_disk_size = random.randint(CONFIG["disk_size_from"], CONFIG["disk_size_to"])
    new_field = f'{field_name} "{random_disk_size}GB"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # scsi0:0.vendorID
    field_name = "scsi0:0.vendorID ="
    field = find_field(field_name)
    random_vendor_name = random.choice(SSD)
    new_field = f'{field_name} "{random_vendor_name}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # cpuid.brandstring
    field_name = "cpuid.brandstring ="
    field = find_field(field_name)
    processor = random.choice(PROCESSORS)
    new_field = f'{field_name} "{processor}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # uuid.bios
    field_name = "uuid.bios ="
    field = find_field(field_name)
    uuid_bios = binascii.hexlify(os.urandom(8), " ").decode() + "-" + binascii.hexlify(os.urandom(8), " ").decode()
    new_field = f'{field_name} "{uuid_bios}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # uuid.location
    field_name = "uuid.location ="
    field = find_field(field_name)
    new_field = f'{field_name} "{uuid_bios}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # hdd.serial
    field_name = "hdd.serial ="
    field = find_field(field_name)
    # rand_hdd_serial_hex_11 = str(random.randint(1, 9)) + binascii.hexlify(os.urandom(5)).decode().upper()
    rand_hdd_serial_hex_12 = binascii.hexlify(os.urandom(6)).decode().upper()
    new_field = f'{field_name} "{rand_hdd_serial_hex_12}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # ethernet1.address
    field_name = "ethernet1.address ="
    field = find_field(field_name)

    match MAC_TYPE:
        case 1:
            random_ethernet_address_hex_6 = binascii.hexlify(os.urandom(6), ":").decode().upper()
        case 2:
            random_ethernet_address_hex_6 = RandMac("00:00:00:00:00:00", True).mac.upper()
        case 3:
            random_ethernet_address_hex_6 = RandMac("00:00:00:00:00:00").mac.upper()
        case 4:
            random_ethernet_address_hex_6 = f"02:00:00:{random.randint(0, 255):02X}:" \
                                            f"{random.randint(0, 255):02X}:" \
                                            f"{random.randint(0, 255):02X}"

    new_field = f'{field_name} "{random_ethernet_address_hex_6}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # ethernet0.address
    field_name = "ethernet0.address ="
    field = find_field(field_name)
    new_field = f'{field_name} "{random_ethernet_address_hex_6}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")

    # sata0:0.fileName
    field_name = "sata0:0.fileName ="
    field = find_field(field_name)
    new_field = f'{field_name} "{WINDOWS_PATH}"'
    DownloadedVm.replace_vm(field, new_field)
    logger.info(f"\n{field} ↓ \n{new_field}")
    save_vm(f'{CREATED_VM_NAME}_{rand_hdd_serial_hex_12}', DownloadedVm.data)
