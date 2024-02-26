from modules.module import IModule
from utilities.config import ICUE_SETUP_PATH


class ICue(IModule):
    def __init__(self):
        IModule.__init__(self, "Install iCue")

    def run(self):
        self.install(ICUE_SETUP_PATH)
