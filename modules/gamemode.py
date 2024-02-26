from modules.module import IModule
import winreg
from utilities.utilities import set_reg_key


class GameMode(IModule):
    def __init__(self):
        IModule.__init__(self, "GameMode")

    def run(self):
        set_reg_key(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\GameBar", "AutoGameModeEnabled", winreg.REG_DWORD,
                    0)
        set_reg_key(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\GameBar", "AllowAutoGameMode", winreg.REG_DWORD, 0)

        set_reg_key(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
                    "AppCaptureEnabled", winreg.REG_DWORD, 0)

        set_reg_key(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
                    "HistoricalCaptureEnabled", winreg.REG_DWORD, 0)

        set_reg_key(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
                    "AppCaptureEnabled", winreg.REG_DWORD, 0)

        self.log("Disabled Game Mode.")
