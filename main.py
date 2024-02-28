import logging
import sys
from tkinter import messagebox

from interface.select_modules import SelectModules
from modules.updates import Updates
from utilities.session import should_update, is_initial_launch, tick_updater

# Setup file to log to with level DEBUG
logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)
# Silence the DEBUG messages from PIL, as it spams the log
logging.getLogger('PIL').setLevel(logging.INFO)
# Create a log handler that points to stdout
handler = logging.StreamHandler(sys.stdout)
# Set its level to INFO
handler.setLevel(logging.INFO)
# Add handler to logger
logging.getLogger().addHandler(handler)

# Check for Windows updates before going to modules
if should_update() and not is_initial_launch():
    logging.info('Need to run updates again. ' + str(is_initial_launch()))
    # run updates
    tick_updater()
    Updates().run()
else:
    select_gui = SelectModules()
    select_gui.run()

# messagebox.showinfo("PicoProof Installer", "Hit OK when done installing software.")

