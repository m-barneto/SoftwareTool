from modules.module import IModule
from utilities.config import SUPERPOSITION_SETUP_PATH


class Superposition(IModule):
    def __init__(self):
        IModule.__init__(self, "Superposition")

    def run(self):
        self.install(SUPERPOSITION_SETUP_PATH)
