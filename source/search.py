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

    def __add_int_to_dict(self, new_item: str, book: dict):
        if new_item not in book:
            book[new_item] = 1
        else:
            book[new_item] += 1

    def __add_value_to_dict(self, new_item: dict, book: dict):
        for key in new_item:
            item_name = key
            count = new_item[key]

        if item_name not in book:
            book[item_name] = count
        else:
            book[item_name] += count

    def set_requirements(self, reqs: dict):
        self.requirements = reqs
        for item in self.requirements:
            self.final_items.append(item)

        # calculating ratios:
        for key in reqs:
            item_request_count = reqs[key]
        item_output_count = self.bd.recipes[item]["out"][item]
        output_to_recipe_ratio: float = (
            item_request_count / item_output_count
        )
        print("request ratio: ", output_to_recipe_ratio)

        self.find_requirements(self.requirements, item_request_count)

    def find_requirements(self, reqs: dict, item_request_count: int):

        items_to_visit: list = []  # list of tuples?
        items_to_visit.append(reqs)
        input_is_raw_resource: bool = False

        while items_to_visit != []:
            item = items_to_visit.pop()
            for key in item:
                global count
                count = item[key]
            item = list(item.keys())[0]

            # set to false every loop
            input_is_raw_resource = False

            # finding in recipes first, then resources
            try:
                item_book = self.bd.recipes[item]
            except KeyError:
                item_book = None
            if item_book is None:
                try:
                    item_book = self.bd.resources[item]
                    # set here, as if its not found then
                    # it will get reset next loop
                except KeyError:
                    print(f"Error! Unable to find '{
                          item}' within recipes or resources book")
                    return

            machine: str = item_book["machine"]
            machine_power_mw: int = self.bd.machines[machine]["power_mw"]

            item_output: dict = item_book["out"]
            item_input: dict = item_book["in"]

            # TODO: delete this block for debugging later
            print("\nITEM:", item)
            print("OUT: ", item_output)
            print("IN:  ", item_input)

            # adding machines and power requirements
            self.__add_int_to_dict(machine, self.machines_needed)
            self.power_mw_needed += machine_power_mw

            # NOTE: now working on items, not machines
            if item_input == 0:
                # early return due to no inputs for current item
                return

            # check for input being a raw resource
            if list(item_input.keys())[0] in self.bd.resources:
                input_is_raw_resource = True

            # adding item to intermediate materials
            if (
                list(item_input.keys())[0] not in self.final_items and
                not input_is_raw_resource
            ):  # classified as not a raw resource or final item
                self.__add_value_to_dict(item_input,
                                         self.inter_materials)
            elif (
                input_is_raw_resource
            ):  # classified as a raw resource, and not a final item
                # THIS is where we need to do the math
                self.__add_value_to_dict(item_input, self.raw_materials)
                pass

            # add the inputs to the items_to_visit list
            if item_input != 0:
                items_to_visit.append(item_input)
