import os
import sys
from config import get_config

def run():
    config = get_config()
    initialize_repo()
    print(config)
    command = f"sudo ./build.sh -d {config['device']} -u {config['ui']} -a {config['arch']} -h {config['hostname']}"
    print(command)
    os.system(command)
    if config['storage'] != "undefined":
        os.system(f"sudo dd if=build/*.img of=/dev/{config['storage']} bs=4M status=progress")
    sys.exit()