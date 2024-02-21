from modules.module import IModule
from utilities.config import ICUE_SETUP_PATH
from utilities.utilities import run

import os


class ICue(IModule):
    def __init__(self):
        IModule.__init__(self, "Install iCue")

    def run(self):
        if os.path.exists(ICUE_SETUP_PATH):
            self.log("Running installer.")
            setup = [ICUE_SETUP_PATH, "--quiet"]
            installed = run(setup)
            if installed == 0:
                self.log("Installed.")
            else:
                self.log("Unable to install.")
        else:
            self.log("Unable to locate installer.")
