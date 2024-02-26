import shutil

from modules.module import IModule
from utilities.config import SHOW_EULA_SYSPREP_PATH
from utilities.utilities import run


class SysPrep(IModule):
    def __init__(self):
        IModule.__init__(self, "SysPrep")

    def run(self):
        shutil.copyfile(SHOW_EULA_SYSPREP_PATH, SHOW_EULA_SYSPREP_PATH)
        # C:\Windows\System32\Sysprep\sysprep.exe /oobe /shutdown /unattend:C:/Windows/showeula.xml
        sysprep = ['C:/Windows/System32/Sysprep/sysprep.exe', "/oobe", "/shutdown", "/unattend:C:/Windows/showeula.xml"]
        run(sysprep)
