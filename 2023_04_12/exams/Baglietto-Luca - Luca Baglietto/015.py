from random import randint

def genera_mac():
    return ':'.join(hex(randint(0, 255))[2:].upper() for _ in range(6))
