import winreg
import subprocess


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
