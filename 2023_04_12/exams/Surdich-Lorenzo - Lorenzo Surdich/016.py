import platform

def sistema_operativo():
    sistema = platform.system()
    versione = platform.release()
    
    if sistema == "Windows":
        return f"Sistema operativo: Windows {versione}"
    elif sistema == "Linux":
        distro = platform.dist()[0]
        return f"Sistema operativo: {distro} {versione}"
    elif sistema == "Darwin":
        return f"Sistema operativo: macOS {versione}"
    else:
        return "Sistema operativo non riconosciuto"

print(sistema_operativo())