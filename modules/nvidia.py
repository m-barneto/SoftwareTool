import os

from modules.module import IModule
from utilities.config import NVIDIA_SETUP_PATH
from utilities.utilities import run


class NVIDIA(IModule):
    def __init__(self):
        IModule.__init__(self, "NVIDIA")

    def run(self):
        if os.path.exists(NVIDIA_SETUP_PATH):
            self.log("Running installer.")
            setup = [NVIDIA_SETUP_PATH, "-s", "-n"]
            installed = run(setup)
            if installed == 0:
                self.log("Installed.")
            else:
                self.log("Unable to install.")
        else:
            self.log("Unable to locate installer.")
