# search class to look find the ingredients needed

from data_initializer import BookData


class Search():
    def __init__(self):
        self.bd = BookData()

        self.requirements: dict = {}
        self.final_items: list[str] = []

        self.raw_materials: dict = {}
        self.inter_materials: dict = {}
        self.machines_needed: dict = {}
        self.power_mw_needed: dict = {}

    def add_to_dict(self, new_item: str, book: dict):
        for item in book:
            if new_item == item:
                book[item] += 1
            else:
                book[new_item] = 1

    def set_requirements(self, reqs: dict):
        self.requirements = reqs
        for item in self.requirements:
            self.final_items.append(item)

        self.r_find_requirements(self.requirements)

    def r_find_requirements(self, reqs: dict):

        items_to_visit: list = []
        items_to_visit.append(reqs)

        while items_to_visit != []:
            item = items_to_visit.pop()
            for key in item:
                global count
                count = item[key]
            item = list(item.keys())[0]

            try:
                item_book = self.bd.recipes[item]
            except KeyError:
                try:
                    item_book = self.bd.resources[item]
                except KeyError:
                    print(f"Error Unable to find {item} within resources book")
                print(f"Error Unable to find {item} within recipes book.")
                return

            machine: str = item_book["machine"]

            item_output: dict = item_book["out"]
            item_input: dict = item_book["in"]

            self.add_to_dict(machine, self.machines_needed)

            if list(item_output.keys())[0] not in self.final_items:
                self.add_to_dict(list(item_output.keys())[0],
                                 self.inter_materials)

            # add the inputs to the items_to_visit list
            if item_input != 0:
                items_to_visit.append(item_input)
