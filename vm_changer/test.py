import binascii
import os
import random
import uuid
import random
import string

from loguru import logger
from randmac import RandMac

# r = RandMac("00:00:00:00:00:00")
# print(r.mac.upper())
from vm_changer.config.config import RANDOM_VM_NAME_LOWERCASE_ONLY


def get_mac():
    return


# a = f"02:00:00:{get_mac():02X}:{get_mac():02X}:{get_mac():02X}"
# print(a)
# "02:00:00:%02x:%02x:%02x"
#
# print("02:00:00:%02x:%02x:%02X" % (random.randint(0, 255),
#                                    random.randint(0, 255),
#                                    random.randint(0, 255)))

random_ethernet_address_hex_6 = binascii.hexlify(os.urandom(6), ":").decode().upper()

print(random_ethernet_address_hex_6)


# print(uuid.SafeUUID)
# print(int(os.urandom(1)))
def get_even_integer():
    while True:
        x = os.urandom(1)
        p = binascii.hexlify(x)
        int_pre = int(p, 16)
        if int_pre == 0:
            return p.decode().upper()
        elif int_pre % 2 == 0:
            return p.decode().upper()


# random_ethernet_address_hex_62 = get_even_integer() + ":" + get_even_integer() + ":" + binascii.hexlify(os.urandom(4),
#                                                                                                         ":").decode().upper()
# random_ethernet_address_hex_6 = f'{get_even_integer()}:{get_even_integer()}:{binascii.hexlify(os.urandom(4), ":").decode().upper()}'
# print(random_ethernet_address_hex_62)
# print(random_ethernet_address_hex_6)

# print(random.seed())
letters = string.ascii_lowercase if RANDOM_VM_NAME_LOWERCASE_ONLY else string.ascii_letters


def get_random_vm_name(k):
    return ''.join(random.choices(letters, k=k))


print(get_random_vm_name(3))

# # print(os.urandom(2)+os.urandom(4))
# print(pre+":".encode()+end)
# logger.debug(binascii.hexlify(os.urandom(1), ":"))
# binascii.hexlify(os.urandom(6), ":")
# print(random_ethernet_address_hex_6)
