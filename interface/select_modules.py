import tkinter as tk
from interface.widgets import CheckboxImage
from modules.armourycrate import ArmouryCrate
from modules.gamemode import GameMode
from modules.icue import ICue
from modules.lconnect import LConnect
from modules.magician import Magician
from modules.msicenter import MsiCenter
from modules.nvidia import NVIDIA
from modules.nzxt import NZXT
from modules.powerplan import PowerPlan
from modules.superposition import Superposition
from modules.updates import Updates
from modules.wallpaper import Wallpaper

from utilities.config import WALLPAPER_COPY_DIR, WALLPAPER_SOURCE
from utilities.utilities import get_path, get_mobo_manu, has_samsung_drive, has_nvidia_gpu, get_nvidia_versions


class SelectModules:
    def __init__(self):
        self.modules = {}
        self.window = tk.Tk()
        self.window.title("PicoProof Installer")
        self.window.geometry("370x625")
        self.window.tk.call('tk', 'scaling', 2.0)
        self.window.config(bg="#303030")

        self.selected_nvidia_version = 'latest'

        self.setup_options()

    def run(self):
        self.window.mainloop()

    def setup_options(self):
        chk_wallpaper = CheckboxImage(Wallpaper(WALLPAPER_COPY_DIR, WALLPAPER_SOURCE), self.window, text="Wallpaper")
        chk_wallpaper.grid(row=0, sticky='w', pady=5)
        self.modules[chk_wallpaper['text']] = chk_wallpaper
        chk_gamemode = CheckboxImage(GameMode(), self.window, text="GameMode")
        chk_gamemode.grid(row=1, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_gamemode
        chk_powerplan = CheckboxImage(PowerPlan(), self.window, text="PowerPlan")
        chk_powerplan.grid(row=2, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_powerplan

        chk_nvidia = CheckboxImage(NVIDIA(), self.window, text="NVIDIA Drivers")
        chk_nvidia.grid(row=3, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_nvidia

        chk_updates = CheckboxImage(Updates(), self.window, text="Windows Updates")
        chk_updates.grid(row=4, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_updates

        chk_msi_center = CheckboxImage(MsiCenter(), self.window, text="MSI Center")
        chk_msi_center.grid(row=5, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_msi_center
        chk_armoury_crate = CheckboxImage(ArmouryCrate(), self.window, text="Armoury Crate")
        chk_armoury_crate.grid(row=6, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_armoury_crate

        chk_superposition = CheckboxImage(Superposition(), self.window, text="Superposition")
        chk_superposition.grid(row=7, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_superposition
        chk_icue = CheckboxImage(ICue(), self.window, text="ICue")
        chk_icue.grid(row=8, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_icue
        chk_nzxt = CheckboxImage(NZXT(), self.window, text="NZXT")
        chk_nzxt.grid(row=9, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_nzxt
        chk_lconnect = CheckboxImage(LConnect(), self.window, text="LConnect")
        chk_lconnect.grid(row=10, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_lconnect
        chk_magician = CheckboxImage(Magician(), self.window, text="Samsung Magician")
        chk_magician.grid(row=11, sticky='w')
        self.modules[chk_wallpaper['text']] = chk_magician

        self.selected_nvidia_version = tk.StringVar(value=get_nvidia_versions()[0])
        lbl_nvidia_versions = tk.OptionMenu(self.window, self.selected_nvidia_version, *get_nvidia_versions())
        lbl_nvidia_versions.grid(row=3, column=1, sticky='e')

    def set_recommended(self):
        self.uncheck_all()

        self.modules['Wallpaper'].update_image(True)
        self.modules['Superposition'].update_image(True)
        # check if amd maybe?

        self.modules['GameMode'].update_image(True)
        self.modules['PowerPlan'].update_image(True)

        # If nvidia gpu installed
        if has_nvidia_gpu():
            self.modules['NVIDIA Drivers'].update_image(True)

        self.modules['Windows Updates'].update_image(True)

        # if msi mobo
        manu = get_mobo_manu()
        if manu is not None:
            if 'asus' in manu:
                self.modules['Armoury Crate'].update_image(True)
            elif 'msi' in manu:
                self.modules['MSI Center'].update_image(True)

        # Check if samsung ssd installed
        if has_samsung_drive():
            self.modules['Samsung Magician'].update_image(True)

    def uncheck_all(self):
        for module in self.modules.keys():
            self.modules[module].update_image(False)

    def install(self):
        self.window.destroy()
        print("Starting installs.")

        for module in self.modules.keys():
            if self.modules[module].module.module_name == "NVIDIA":
                self.modules[module].module.set_nvidia_version(self.selected_nvidia_version.get())
            self.modules[module].run()
