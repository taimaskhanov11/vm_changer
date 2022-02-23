import random
from randmac import RandMac


# r = RandMac("00:00:00:00:00:00")
# print(r.mac.upper())
def get_mac():
    return


a = f"02:00:00:{get_mac():02X}:{get_mac():02X}:{get_mac():02X}"
print(a)
"02:00:00:%02x:%02x:%02x"

print("02:00:00:%02x:%02x:%02X" % (random.randint(0, 255),
                                   random.randint(0, 255),
                                   random.randint(0, 255)))
