from fetch import initialize_repo
from simple_term_menu import TerminalMenu

def choose_repo():
    sources = ["dreemurrs-embedded/arch-pine64-build", "arch-pine64-build2"]
    options = ["dreemurrs-embedded/", "arch-pine64-build2"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return dirs[menu_entry_index]