

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/015.py
#
from random import randint

def genera_mac():
    return ':'.join(hex(randint(0, 255))[2:].upper() for _ in range(6))


# -----------------------
# ./roggero_costantino/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./lin-matteo - Matth6ew/015.py
#
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

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./molinari-giorgia/015.py
#
import random

def genera_mac():
    # Genera 6 coppie di cifre esadecimali
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    # Formatta l'indirizzo MAC con due cifre esadecimali separate da due punti
    mac_string = ':'.join(['{:02X}'.format(c) for c in mac])
    return mac_string

# Esempi di utilizzo della funzione
mac1 = genera_mac()
print("Indirizzo MAC generato 1:", mac1)

mac2 = genera_mac()
print("Indirizzo MAC generato 2:", mac2)

mac3 = genera_mac()
print("Indirizzo MAC generato 3:", mac3)

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/015.py
#
import random

def genera_mac():
    # Genera 6 coppie di cifre esadecimali
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    # Formatta l'indirizzo MAC con due cifre esadecimali separate da due punti
    mac_string = ':'.join(['{:02X}'.format(c) for c in mac])
    return mac_string

# Esempi di utilizzo della funzione
mac1 = genera_mac()
print("Indirizzo MAC generato 1:", mac1)

mac2 = genera_mac()
print("Indirizzo MAC generato 2:", mac2)

mac3 = genera_mac()
print("Indirizzo MAC generato 3:", mac3)

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/015.py
#
import random

def genera_mac():
    char_set = "ABCDEF0123456789"
    mac_addr = ""
    due_punti = 0

    for _ in range(6):
        for _ in range(2):
            mac_addr += random.choice(char_set)
        if due_punti < 5:
          mac_addr += ":"
          due_punti += 1

    return mac_addr

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./alessandro-lugaro/015.py
#
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

# -----------------------
# ./botta-alessio - Alessio Botta/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./esercizi informatica minetti giulio - Giulio Minetti/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/015.py
#
import random

def genera_mac():
    mac = [0]*6
    for i in range(6):
        mac[i] = random.randint(0, 255)
    return ':'.join('{:02x}'.format(b) for b in mac)

genera_mac(0)

# -----------------------
# ./dapino-berenice/015.py
#


# -----------------------
# ./portella-francesco - Francesco Portella/015.py
#
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

# -----------------------
# ./moretti-christian/015.py
#
import random

def genera_mac():
    # Genera 6 coppie di cifre esadecimali
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    # Formatta l'indirizzo MAC con due cifre esadecimali separate da due punti
    mac_string = ':'.join(['{:02X}'.format(c) for c in mac])
    return mac_string

# Esempi di utilizzo della funzione
mac1 = genera_mac()
print("Indirizzo MAC generato 1:", mac1)

mac2 = genera_mac()
print("Indirizzo MAC generato 2:", mac2)

mac3 = genera_mac()
print("Indirizzo MAC generato 3:", mac3)

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./hu-xuan-di/015.py
#
import random

def genera_mac():
    # Genera 6 coppie di cifre esadecimali
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    # Formatta l'indirizzo MAC con due cifre esadecimali separate da due punti
    mac_string = ':'.join(['{:02X}'.format(c) for c in mac])
    return mac_string

# Esempi di utilizzo della funzione
mac1 = genera_mac()
print("Indirizzo MAC generato 1:", mac1)

mac2 = genera_mac()
print("Indirizzo MAC generato 2:", mac2)

mac3 = genera_mac()
print("Indirizzo MAC generato 3:", mac3)

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/015.py
#
import random

def genera_mac():
    # Genera 6 coppie di cifre esadecimali
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    # Formatta l'indirizzo MAC con due cifre esadecimali separate da due punti
    mac_string = ':'.join(['{:02X}'.format(c) for c in mac])
    return mac_string

# Esempi di utilizzo della funzione
mac1 = genera_mac()
print("Indirizzo MAC generato 1:", mac1)

mac2 = genera_mac()
print("Indirizzo MAC generato 2:", mac2)

mac3 = genera_mac()
print("Indirizzo MAC generato 3:", mac3)

genera_mac()

# -----------------------
# ./zono veran - Fabrizio Verani/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/015.py
#
import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out

# -----------------------
# ./Matteo-Marazzi/015.py
#
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