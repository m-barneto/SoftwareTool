import os
import threading

from modules.module import IModule
from utilities.utilities import run, get_nvidia_setup


class NVIDIA(IModule):
    def __init__(self):
        self.nvidia_version = "latest"
        IModule.__init__(self, "NVIDIA")

    def set_nvidia_version(self, version):
        self.nvidia_version = version

    def run(self):
        nvidia_setup = get_nvidia_setup(self.nvidia_version)
        if os.path.exists(nvidia_setup):
            self.log("Running installer.")
            setup = [nvidia_setup, "-s", "-n"]
            installed = run(setup)
            if installed == 0:
                self.log("Installed.")
            else:
                self.log("Unable to install.")
        else:
            self.log("Unable to locate installer.")
