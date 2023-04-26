import platform

def get_os_info():
    os_name = platform.system()
    os_release = platform.release()

    os_info = f"Sistema Operativo: {os_name}\nRelease: {os_release}"
    return os_info

os_info = get_os_info()
print(os_info)