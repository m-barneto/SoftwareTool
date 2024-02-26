from modules.module import IModule
from utilities.powershell import install_updates


class Updates(IModule):
    def __init__(self):
        IModule.__init__(self, "Windows Updates")

    def run(self):
        install_updates()

