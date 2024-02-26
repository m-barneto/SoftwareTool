import os

from modules.module import IModule
from utilities.config import SAMSUNG_MAGICIAN_SETUP_PATH
from utilities.utilities import run


class Magician(IModule):
    def __init__(self):
        IModule.__init__(self, "Samsung Magician", True)

    def run(self):
        self.install(SAMSUNG_MAGICIAN_SETUP_PATH)
