import random

def genera_mac():
    mac = [0]*6
    for i in range(6):
        mac[i] = random.randint(0, 255)
    return ':'.join('{:02x}'.format(b) for b in mac)

genera_mac(0)