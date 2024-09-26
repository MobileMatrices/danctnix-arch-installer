import os

def initialize_repo():
    path = os.path.expanduser("~/.local/var")
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    if os.path.isdir("arch-pine64-build"):
        os.chdir("arch-pine64-build")
        os.system("git fetch")
    else:
        os.system("git clone https://github.com/dreemurrs-embedded/arch-pine64-build")
        os.chdir("arch-pine64-build")