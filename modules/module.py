class IModule:
    def __init__(self, module_name):
        self.module_name = module_name
        self.run()

    def run(self):
        pass

    def log(self, msg):
        print(self.module_name + ": " + msg)
