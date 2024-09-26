from simple_term_menu import TerminalMenu
from config import update_config, get_config

def user_interface():
    dirs = ["barebone", "phosh", "plasma_desktop", "plasma", "sxmo"]
    options = ["Barebone", "Phosh", "Plasma Desktop", "Plasma Mobile", "SXMO"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    update_config("ui", dirs[menu_entry_index])

def device():
    dirs = ['pinephone', 'pinephone-pro', 'pinetab', 'pinetab2']
    options = ["Pinephone", "Pinephone Pro", "PineTab", "Pinetab2"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    update_config("device", dirs[menu_entry_index])

def architecture():
    options = ["aarch64", "armhf"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    update_config("arch", options[menu_entry_index])

def hostname():
    hostname = input("Enter a hostname: ")
    update_config("hostname", hostname)

def storage(list_block_devices):
    devices_info = list_storage()
    for info in devices_info:
        print(info)
    storage_device = input("Enter the storage device: ")
    update_config("storage", storage_device)