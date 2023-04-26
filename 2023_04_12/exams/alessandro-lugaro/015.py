import random

def genera_mac():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    mac_string = ':'.join(['{:02X}'.format(c) for c in mac])
    return mac_string

mac1 = genera_mac()
print("Indirizzo MAC generato 1:", mac1)

mac2 = genera_mac()
print("Indirizzo MAC generato 2:", mac2)

mac3 = genera_mac()
print("Indirizzo MAC generato 3:", mac3)