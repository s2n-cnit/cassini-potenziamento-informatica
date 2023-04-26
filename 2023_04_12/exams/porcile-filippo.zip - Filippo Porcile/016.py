import platform

def get_os_info():
    # Ottiene il nome del Sistema Operativo
    os_name = platform.system()
    # Ottiene la release del Sistema Operativo
    os_release = platform.release()

    # Restituisce una stringa formattata con le informazioni ottenute
    os_info = f"Sistema Operativo: {os_name}\nRelease: {os_release}"
    return os_info

# Esempio di utilizzo della funzione
os_info = get_os_info()
print(os_info)