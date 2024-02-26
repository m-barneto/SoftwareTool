import os

from modules.module import IModule
from utilities.config import ARMOURY_CRATE_SETUP_PATH
from utilities.utilities import run


class ArmouryCrate(IModule):
    def __init__(self):
        IModule.__init__(self, "Armoury Crate", True)

    def run(self):
        self.install(ARMOURY_CRATE_SETUP_PATH)
