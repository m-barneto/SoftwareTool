import os

from modules.module import IModule
from utilities.config import MSICENTER_SETUP_PATH
from utilities.utilities import run


class MsiCenter(IModule):
    def __init__(self):
        IModule.__init__(self, "Msi Center")

    def run(self):
        if os.path.exists(MSICENTER_SETUP_PATH):
            self.log("Running installer.")
            setup = [MSICENTER_SETUP_PATH, "/norestart", "/verysilent"]
            installed = run(setup)
            if installed == 0:
                self.log("Installed.")
            else:
                self.log("Unable to install.")
        else:
            self.log("Unable to locate installer.")
