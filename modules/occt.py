import os
import shutil

from modules.module import IModule
from utilities.config import OCCT_SETUP_PATH


class OCCT(IModule):
    def __init__(self):
        IModule.__init__(self, "OCCT")

    def run(self):
        shutil.copyfile(OCCT_SETUP_PATH, os.path.expanduser("~/Desktop/OCCT.exe"))
        self.log("Copied OCCT to user desktop.")
