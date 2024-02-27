import os
import logging

from utilities.utilities import run


class IModule:
    threads = []

    def __init__(self, module_name, manual=False):
        self.module_name = module_name
        self.manual = manual
        logging.debug("Initializing module " + self.module_name)

    def run(self):
        pass

    def log(self, msg):
        logging.info(self.module_name + ": " + msg)

    def install(self, installer_path):
        logging.debug("Installing module " + self.module_name)
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
