import logging
import sys
from tkinter import messagebox

from interface.select_modules import SelectModules

# Setup file to log to with level DEBUG
logging.basicConfig(filename='log.txt', filemode='a', level=logging.DEBUG)
# Silence the DEBUG messages from PIL, as it spams the log
logging.getLogger('PIL').setLevel(logging.INFO)
# Create a log handler that points to stdout
handler = logging.StreamHandler(sys.stdout)
# Set its level to INFO
handler.setLevel(logging.INFO)
# Add handler to logger
logging.getLogger().addHandler(handler)

logging.info("New instance started.")

select_gui = SelectModules()
select_gui.run()

logging.info("GUI run.")
# MsiCenterAutomation()


messagebox.showinfo("PicoProof Installer", "Hit OK when done installing software.")
logging.info("called msgbox")

