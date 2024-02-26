# retcode = subprocess.Popen(args, stdout=sys.stdout)
import subprocess
import sys

from utilities.config import UPDATE_WINDOWS_PS


def install_updates():
    p = subprocess.Popen(f'powershell.exe -ExecutionPolicy RemoteSigned -file "{UPDATE_WINDOWS_PS}"', stdout=sys.stdout)
    p.communicate()
