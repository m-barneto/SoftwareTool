import os

from modules.module import IModule
from utilities.config import SUPERPOSITION_SETUP_PATH
from utilities.utilities import run


class Superposition(IModule):
    def __init__(self):
        IModule.__init__(self, "Superposition")

    def run(self):
        if os.path.exists(SUPERPOSITION_SETUP_PATH):
            self.log("Running installer.")
            setup = [SUPERPOSITION_SETUP_PATH, "/verysilent", "/norestart"]
            installed = run(setup)
            if installed == 0:
                self.log("Installed.")
            else:
                self.log("Unable to install.")
        else:
            self.log("Unable to locate installer.")
