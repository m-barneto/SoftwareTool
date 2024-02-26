from modules.module import IModule
from utilities.config import NZXT_CAM_SETUP_PATH


class NZXT(IModule):
    def __init__(self):
        IModule.__init__(self, "NZXT Cam")

    def run(self):
        self.install(NZXT_CAM_SETUP_PATH)
