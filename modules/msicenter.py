from modules.module import IModule
from utilities.config import MSICENTER_SETUP_PATH


class MsiCenter(IModule):
    def __init__(self):
        IModule.__init__(self, "Msi Center")

    def run(self):
        self.install(MSICENTER_SETUP_PATH)
