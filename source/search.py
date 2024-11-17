# search class to look find the ingredients needed

from data_initializer import BookData


class Search():
    def __init__(self):
        self.bd = BookData()

        self.requirements: dict = {}

        self.raw_materials: dict = {}
        self.inter_materials: dict = {}
        self.machines_needed: dict = {}
        self.power_mw_needed: dict = {}

    def set_requirements(self, reqs: dict):
        self.requirements = reqs

        for item in self.requirements:
            count = self.requirements[item]

            try:
                item_book = self.bd.recipes[item]
            except KeyError:
                print(f"Error! Unable to find {item} within recipe book.")
            finally:
                pass
