import os
import sys
import winreg
import subprocess

import wmi

from utilities.config import NVIDIA_VERSIONS_DIRECTORY


def set_reg_key(key, sub_key, name, value_type, value):
    with winreg.OpenKey(key, sub_key, 0, winreg.KEY_WRITE) as registry_key:
        winreg.SetValueEx(registry_key, name, 0, value_type, value)


def run(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode == 0:
        return result.returncode
    command_str = " ".join(command)
    print("Error running: " + command_str)
    print(result.returncode, result.stdout, result.stderr)
    return result.returncode


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        print('meipass')
        return os.path.join(sys._MEIPASS, filename)
    else:
        return os.path.join("./", filename)


def get_mobo_manu():
    c = wmi.WMI()
    query = "select * from " + "Win32_BaseBoard"

    mobo_manu = str(c.query(query)[0].wmi_property('Manufacturer').value).strip()

    if 'asus' in mobo_manu.lower():
        return 'asus'
    elif 'micro' in mobo_manu.lower():
        return 'msi'
    else:
        return None


def has_samsung_drive():
    c = wmi.WMI()
    wql = "SELECT * " + "FROM Win32_DiskDrive"
    for disk in c.query(wql):
        model = disk.wmi_property('Caption').value
        if 'samsung' in model.lower():
            return True
    return False


def has_nvidia_gpu():
    c = wmi.WMI()
    wql = "SELECT * " + "FROM win32_VideoController"
    for gpu in c.query(wql):
        model = gpu.wmi_property('Caption').value
        if 'nvidia' in model.lower():
            return True
    return False


def get_nvidia_versions():
    versions = []
    for version in reversed(sorted(os.listdir(NVIDIA_VERSIONS_DIRECTORY))):
        versions.append(version)
    return versions


def get_nvidia_setup(version):
    if version == 'latest':
        return NVIDIA_VERSIONS_DIRECTORY + get_nvidia_versions()[0] + "/setup.exe"
    else:
        return NVIDIA_VERSIONS_DIRECTORY + version + "/setup.exe"

# moboName = str(c.query(query)[0].wmi_property('Product').value)
