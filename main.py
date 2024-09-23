from simple_term_menu import TerminalMenu
import os
import sys

image_config = {
    "ui": 'barebone',
    "device": 'pinephone',
    "arch": "aarch64",
    "hostname": "danctnix",
    "storage": "/dev/mmcblk0"
}
def initialize_repo():
    path = "/home/USER/.local/var"
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    if os.path.isdir("arch-pine64-build"):
        os.chdir("arch-pine64-build")
        os.system("git fetch")
    else:
        os.system("git clone https://github.com/dreemurrs-embedded/arch-pine64-build")
        os.chdir("arch-pine64-build")

def user_interface():
    dirs = ["barebone", "phosh", "plasma_desktop", "plasma", "sxmo"]
    options = ["Barebone", "Phosh", "Plasma Desktop", "Plasma Mobile", "SXMO"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    image_config["ui"] = dirs[menu_entry_index]
def device():
    dirs = ['pinephone', 'pinephone-pro', 'pinetab', 'pinetab2']
    options = ["Pinephone", "Pinephone Pro", "PineTab", "Pinetab2"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    image_config["device"] = dirs[menu_entry_index]
def architecture():
    options = ["aarch64", "armhf"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    image_config["arch"] = options[menu_entry_index]
def hostname():
    image_config["hostname"] = input("Enter a hostname: ")
def list_storage(directory="/dev"):
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)) and (file.startswith("sd") or file.startswith("mmcblk"))]


def storage():
    os.system("lsblk")
    image_config["storage"] = input("Enter the storage device: ")
def run():
    initialize_repo()

    print(image_config)
    # generate image
    command = "sudo ./build.sh -d "+ image_config['device'] + " -u " + image_config['ui'] + " -a " + image_config['arch'] + " -h " + image_config['hostname']
    print(command)
    os.system(command)
    sys.exit()
def main():
    funcs = [device, user_interface, architecture, hostname, storage, run, sys.exit]
    options = ["Device", "User Interface", "Architecture", "Hostname", "Storage", "Continue", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    funcs[menu_entry_index]()
    if menu_entry_index != 6:
        main()
    #print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()