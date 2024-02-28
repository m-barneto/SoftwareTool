from modules.module import IModule
from utilities.config import SUPERPOSITION_SETUP_PATH, CREATE_SUPERPOSITION_UNINSTALLER


class Superposition(IModule):
    def __init__(self):
        IModule.__init__(self, "Superposition")

    def run(self):
        if CREATE_SUPERPOSITION_UNINSTALLER:
            with open('C:\\Users\\PC\\Desktop\\unins superposition.bat', 'w+') as unins:
                unins.write('"C:\\Program Files\\Unigine\\Superposition Benchmark\\unins000.exe"')
        self.install(SUPERPOSITION_SETUP_PATH)
