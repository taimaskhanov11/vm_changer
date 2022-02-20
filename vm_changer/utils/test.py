import binascii
import os
import random
import secrets
import uuid


def get_rand() -> str:
    res = str(random.randint(0, 999999999999))
    if len(res) < 12:
        zeros = 12 - len(res)
        res = "0" * zeros + res
    return res

def hex_rand():
    # a = binascii.b2a_hex(os.urandom(6))
    hex_number = binascii.hexlify(os.urandom(6), ":")
    print(hex_number.decode().upper())
    print(len(str(hex_number)))

def get_uuid_rand():
    uuid_bios_l = binascii.hexlify(os.urandom(8), " ").decode()
    uuid_bios_r = binascii.hexlify(os.urandom(8), " ").decode()
    return uuid_bios_l + "-" + uuid_bios_r
    # 56 4d 55 03 fe 1d 20 75-f7 01 d8 3c 87 14 73 6b

def get_hdd_setial():
    hdd_serial = os.urandom(5)
    rand_hdd_serial = binascii.hexlify(hdd_serial).decode().upper()
    print(rand_hdd_serial)
    print(str(random.randint(1, 9))+rand_hdd_serial)

# get_hdd_setial()
# rand_hdd_serial = str(random.randint(1, 9)) + binascii.hexlify(os.urandom(5)).decode().upper()
# print(rand_hdd_serial)
# print('%X' % 19)
# a = secrets.token_bytes()
# print(binascii.hexlify(a))
# print(a.hex())

a = "312312"
b = a[:]

print(id(a))
print(id(b+a))
print(id(b))
