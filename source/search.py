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
        self.power_mw_needed: int = 0

    def __add_to_dict(self, new_item: str, book: dict):
        if new_item not in book:
            book[new_item] = 1
        else:
            book[new_item] += 1

    def set_requirements(self, reqs: dict):
        self.requirements = reqs
        for item in self.requirements:
            self.final_items.append(item)

        self.find_requirements(self.requirements)

    def find_requirements(self, reqs: dict):

        items_to_visit: list = []
        items_to_visit.append(reqs)
        item_is_raw_resource: bool = False

        while items_to_visit != []:
            item = items_to_visit.pop()
            for key in item:
                global count
                count = item[key]
            item = list(item.keys())[0]

            # set to false every loop
            item_is_raw_resource = False

            # finding in recipes first, then resources
            try:
                item_book = self.bd.recipes[item]
            except KeyError:
                item_book = None
            if item_book is None:
                try:
                    item_book = self.bd.resources[item]
                    item_is_raw_resource = True
                    # set here, as if its not found then it will get reset next loop
                except KeyError:
                    print(f"Error! Unable to find '{
                          item}' within recipes or resources book")
                    return

            machine: str = item_book["machine"]
            machine_power_mw: int = self.bd.machines[machine]["power_mw"]

            item_output: dict = item_book["out"]
            item_input: dict = item_book["in"]

            # adding machines and power requirements
            self.__add_to_dict(machine, self.machines_needed)
            self.power_mw_needed += machine_power_mw

            # adding item to intermediate materials
            if (
                list(item_output.keys())[0] not in self.final_items and
                not item_is_raw_resource
            ):
                self.__add_to_dict(list(item_output.keys())[0],
                                   self.inter_materials)
            elif item_is_raw_resource:  # and not a final_items
                self.__add_to_dict(list(item_output.keys())[0],
                                   self.raw_materials)

            # add the inputs to the items_to_visit list
            if item_input != 0:
                items_to_visit.append(item_input)
