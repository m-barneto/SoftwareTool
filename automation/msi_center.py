import subprocess
import time
import cv2

from automation.auto_utils import window_capture
from utilities.config import MSICENTER_SHELL_CMD
from utilities.utilities import run


class MsiCenterAutomation:
    def __init__(self):
        result = subprocess.run(MSICENTER_SHELL_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(result)
        # opens msi center
        time.sleep(1)
        # Using cv2.imshow() method
        # Displaying the image
        cv2.imshow("ss", window_capture())

        # waits for user to press any key
        # (this is necessary to avoid Python kernel form crashing)
        cv2.waitKey(0)

        # closing all open windows
        cv2.destroyAllWindows()

