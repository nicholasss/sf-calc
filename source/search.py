# search class to look find the ingredients needed

class Search():
    def __init__(self):
        self.requirements: dict = {}

        self.raw_materials: dict = {}
        self.inter_materials: dict = {}
        self.machines_needed: dict = {}
        self.power_mw_needed: dict = {}

    def set_requirements(self, requirements: dict):
        pass
