import tkinter as tk

from interface.widgets import CheckboxImage
from modules.armourycrate import ArmouryCrate
from modules.gamemode import GameMode
from modules.icue import ICue
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

modules = []

window = tk.Tk()
window.title("PicoProof Installer")
window.geometry("370x550")
window.tk.call('tk', 'scaling', 2.0)
window.config(bg="#303030")

chkWallpaper = CheckboxImage(Wallpaper(WALLPAPER_COPY_DIR, WALLPAPER_SOURCE), window, text="Wallpaper")
chkWallpaper.grid(row=0, sticky='w', pady=5)
modules.append(chkWallpaper)
chkGameMode = CheckboxImage(GameMode(), window, text="GameMode")
chkGameMode.grid(row=1, sticky='w')
modules.append(chkGameMode)
chkPowerPlan = CheckboxImage(PowerPlan(), window, text="PowerPlan")
chkPowerPlan.grid(row=2, sticky='w')
modules.append(chkPowerPlan)

chkNVIDIA = CheckboxImage(NVIDIA(), window, text="NVIDIA Drivers")
chkNVIDIA.grid(row=3, sticky='w')
modules.append(chkNVIDIA)

chkUpdates = CheckboxImage(Updates(), window, text="Windows Updates")
chkUpdates.grid(row=4, sticky='w')
modules.append(chkUpdates)

chkMSICenter = CheckboxImage(MsiCenter(), window, text="MSI Center")
chkMSICenter.grid(row=5, sticky='w')
modules.append(chkMSICenter)
chkArmouryCrate = CheckboxImage(ArmouryCrate(), window, text="Armoury Crate")
chkArmouryCrate.grid(row=6, sticky='w')
modules.append(chkArmouryCrate)

chkSuperposition = CheckboxImage(Superposition(), window, text="Superposition")
chkSuperposition.grid(row=7, sticky='w')
modules.append(chkSuperposition)
chkICue = CheckboxImage(ICue(), window, text="ICue")
chkICue.grid(row=8, sticky='w')
modules.append(chkICue)
chkNZXT = CheckboxImage(NZXT(), window, text="NZXT")
chkNZXT.grid(row=9, sticky='w')
modules.append(chkNZXT)
chkMagician = CheckboxImage(Magician(), window, text="Samsung Magician")
chkMagician.grid(row=10, sticky='w')
modules.append(chkMagician)

selectedVersion = tk.StringVar(value=get_nvidia_versions()[0])
lbNvidiaVersions = tk.OptionMenu(window, selectedVersion, *get_nvidia_versions())
lbNvidiaVersions.grid(row=3, column=1, sticky='e')


def set_recommended():
    uncheck_all()

    chkWallpaper.update_image(True)
    chkSuperposition.update_image(True)
    # check if amd maybe?
    chkGameMode.update_image(True)
    chkPowerPlan.update_image(True)

    # If nvidia gpu installed
    if has_nvidia_gpu():
        chkNVIDIA.update_image(True)

    chkUpdates.update_image(True)

    # if msi mobo
    manu = get_mobo_manu()
    if manu is not None:
        if 'asus' in manu:
            chkArmouryCrate.update_image(True)
        elif 'msi' in manu:
            chkMSICenter.update_image(True)

    # Check if samsung ssd installed
    if has_samsung_drive():
        chkMagician.update_image(True)


def uncheck_all():
    for module in modules:
        module.update_image(False)


def install():

    window.destroy()
    print("Starting installs.")

    for module in modules:
        if module.module.module_name == "NVIDIA":
            module.module.set_nvidia_version(selectedVersion.get())
        module.run()


btnRecommended = tk.Button(window, text="Recommended", justify="right", anchor="e", command=set_recommended)
btnRecommended.grid(row=0, column=1, sticky='e')

btnUncheckAll = tk.Button(window, text="Uncheck All", justify="right", anchor="e", command=uncheck_all)
btnUncheckAll.grid(row=1, column=1, sticky='e')

btnInstall = tk.Button(window, text="Install", justify="right", anchor="e", relief="groove", command=install)
btnInstall.grid(row=10, column=1, sticky='e')

set_recommended()

window.mainloop()

