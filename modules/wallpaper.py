import ctypes
import shutil

from modules.module import IModule

from utilities.utilities import set_reg_key


class Wallpaper(IModule):
    SPI_SETDESKTOPWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1

    def __init__(self, copy_to_dir, source_file):
        self.copy_to_dir = copy_to_dir
        self.source_file = source_file
        IModule.__init__(self, "Wallpaper")

    def run(self):
        shutil.copyfile(self.source_file, self.copy_to_dir)
        # Set desktop background to PowerGPU image in Pictures
        success = ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKTOPWALLPAPER, 0, self.copy_to_dir, self.SPIF_UPDATEINIFILE)
        if success:
            print("Set desktop wallpaper.")
        else:
            print("Couldn't set desktop wallpaper.")
