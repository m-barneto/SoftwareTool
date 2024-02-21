from modules.module import IModule
from utilities.config import POWERPLAN_GUID
from utilities.utilities import run


class PowerPlan(IModule):
    def __init__(self):
        IModule.__init__(self, "PowerPlan")

    def run(self):
        set_powerplan_cmd = ["powercfg", "-setactive", POWERPLAN_GUID]
        disable_standby_timeout_cmd = ["powercfg", "-change", "-standby-timeout-ac", "0"]
        disable_monitor_timeout_cmd = ["powercfg", "-change", "-monitor-timeout-ac", "0"]

        self.log("Set powerplan.")
        run(set_powerplan_cmd)
        self.log("Disabled sleep.")
        run(disable_monitor_timeout_cmd)
        run(disable_standby_timeout_cmd)
