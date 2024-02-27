from modules.module import IModule
from utilities.config import LCONNECT_SETUP_PATH


class LConnect(IModule):
    def __init__(self):
        IModule.__init__(self, "LConnect", True)

    def run(self):
        self.install(LCONNECT_SETUP_PATH)
