import logging
import shutil
from tkinter import messagebox

from modules.module import IModule
from utilities.config import SHOW_EULA_SYSPREP_PATH
from utilities.utilities import run


class SysPrep(IModule):
    def __init__(self):
        IModule.__init__(self, "SysPrep")

    def run(self):
        logging.info("Starting sysprep.")
        answer = messagebox.askyesno(title="PICO ARE YOU SURE???",
                                     message="Are you sure you want to run the sysprep module?\n"
                                             "Check if you need to do anything else first.",
                                     icon="warning")
        logging.info(answer)
        if not answer:
            logging.info("Cancelling sysprep.")
            return
        logging.info("Running sysprep.")

        shutil.copyfile(SHOW_EULA_SYSPREP_PATH, SHOW_EULA_SYSPREP_PATH)
        # C:\Windows\System32\Sysprep\sysprep.exe /oobe /shutdown /unattend:C:/Windows/showeula.xml
        sysprep = ['C:/Windows/System32/Sysprep/sysprep.exe', "/oobe", "/shutdown", "/unattend:C:/Windows/showeula.xml"]
        run(sysprep)
        logging.info("Ran sysprep command, goodbye!")
