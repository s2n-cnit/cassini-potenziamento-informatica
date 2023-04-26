import platform

def os():
    print(f'OS: {platform.system()}')
    print(f'Release: {platform.release()}')
    print(f'Version: {platform.version()}')
    
os()