import platform

def sis_op():
    print(f'OS: {platform.system()}')
    print(f'Release: {platform.release()}')
    print(f'Version: {platform.version()}')
    
sis_op()