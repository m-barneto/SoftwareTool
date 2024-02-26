import os
import threading

from utilities.utilities import run


class IModule:
    threads = []

    def __init__(self, module_name, manual=False):
        self.module_name = module_name
        self.manual = manual
        # self.run()

    def run(self):
        pass

    def log(self, msg):
        print(self.module_name + ": " + msg)

    def install(self, installer_path):
        if os.path.exists(installer_path):
            self.log("Running installer.")
            if self.manual:
                setup = [installer_path, "/norestart"]
            else:
                setup = [installer_path, "/norestart", "/verysilent"]
            installed = run(setup)
            if installed == 0:
                self.log("Installed.")
            else:
                self.log("Unable to install.")
        else:
            self.log("Unable to locate installer.")
