import os
try:
    import Flask
except ImportError as e:
    print(f'Please install required modules: pip3 install -r requirements.txt. {e}')
    os.system("pip3 install -r requirements.txt")
    raise