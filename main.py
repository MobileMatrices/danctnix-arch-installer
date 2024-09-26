import sys
from simple_term_menu import TerminalMenu
from ui import user_interface, device, architecture, hostname, storage
from build import run
from storage import list_storage
from config import get_config, update_config

def main():
    funcs = [device, user_interface, architecture, hostname, lambda: storage(list_block_devices), run, sys.exit]
    options = [
        f"Device - {get_config()['device']}",
        f"User Interface - {get_config()['ui']}",
        f"Architecture - {get_config()['arch']}",
        f"Hostname - {get_config()['hostname']}",
        f"Storage Device - {get_config()['storage']}",
        "Continue",
        "Exit"
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    funcs[menu_entry_index]()
    if menu_entry_index != 6:
        main()

if __name__ == "__main__":
    main()