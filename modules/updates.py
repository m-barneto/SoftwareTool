from modules.module import IModule
from utilities.powershell import install_updates
from utilities.session import is_initial_launch, tick_updater


class Updates(IModule):
    def __init__(self):
        IModule.__init__(self, "Windows Updates")

    def run(self):
        if is_initial_launch():
            tick_updater()
            install_updates()

