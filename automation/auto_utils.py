from mss import mss
import numpy as np


def window_capture():
    with mss() as sct:
        # Part of the screen to capture
        img = sct.grab(mss().monitors[0])
        img = np.array(img)
    return img
