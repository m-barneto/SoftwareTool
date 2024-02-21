import os

from modules.module import IModule
from utilities.config import SAMSUNG_MAGICIAN_SETUP_PATH
from utilities.utilities import run


class Magician(IModule):
    def __init__(self):
        IModule.__init__(self, "Samsung Magician")

    def run(self):
        if os.path.exists(SAMSUNG_MAGICIAN_SETUP_PATH):
            self.log("Running installer.")
            setup = [SAMSUNG_MAGICIAN_SETUP_PATH, "/norestart"]
            installed = run(setup)
            if installed == 0:
                self.log("Installed.")
            else:
                self.log("Unable to install.")
        else:
            self.log("Unable to locate installer.")
