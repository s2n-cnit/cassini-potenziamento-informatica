import platform


def sys_info():
    print(f"Il Sistema attualmente in uso è: {platform.system()}")
    print(f"Info Release: {platform.release()}")
