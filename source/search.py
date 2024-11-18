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

    def __unpack_dict(self, item: dict) -> (str, int):
        for key in item:
            name = key
            num = item[key]
        return (name, num)

    def __name_in_dict(self, item: dict) -> str:
        for key in item:
            return key

    def __count_in_dict(self, item: dict) -> int:
        for key in item:
            return item[key]

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

        # calculating output ratio:
        item_request_count = self.__count_in_dict(reqs)
        item_output_count = self.bd.recipes[item]["out"][item]
        request_ratio: float = (
            item_request_count / item_output_count
        )
        print("request ratio: ", request_ratio)

        self.find_requirements(self.requirements, request_ratio)

    def find_requirements(self, reqs: dict, request_ratio: float):

        items_to_visit: list = []  # list of tuples?
        items_to_visit.append(reqs)
        input_is_raw_resource: bool = False

        while items_to_visit != []:
            item_page = items_to_visit.pop()
            # item_page is only from reqs first time around,
            # subsequent times, it is an input value from the current recipe
            request_name, request_count = self.__unpack_dict(item_page)
            input_is_raw_resource = False

            # NOTE: pulling information from bookdata class
            try:
                recipe_page = self.bd.recipes[request_name]
            except KeyError:
                recipe_page = None
            if recipe_page is None:
                try:
                    recipe_page = self.bd.resources[request_name]
                    # set here, as if its not found then
                    # it will get reset next loop
                except KeyError:
                    print(f"Error! Unable to find '{
                          request_name}' within recipes or resources book")
                    return

            # NOTE: adding info to machines and power
            # cannot be further down, due to early return
            machine_name: str = recipe_page["machine"]
            machine_power_mw: int = self.bd.machines[machine_name]["power_mw"]
            self.__add_int_to_dict(machine_name, self.machines_needed)
            self.power_mw_needed += machine_power_mw

            # NOTE: readying input/output information
            output_dict: dict = recipe_page["out"]
            input_dict: dict = recipe_page["in"]
            if input_dict == 0:
                # early return due to no inputs for current item
                return

            output_name, output_count = self.__unpack_dict(output_dict)
            input_name, input_count = self.__unpack_dict(input_dict)
            # check for input being a raw resource
            if input_name in self.bd.resources:
                input_is_raw_resource = True

            # NOTE: calculations for how many inputs/machines needed
            if request_ratio != 1.0:
                print("performing ratio calculations")

            # TODO: delete this block for debugging later
            print("\nITEM:", request_name)
            print("OUT: ", output_name, output_count)
            print("IN:  ", input_name, input_count)

            # NOTE: adding info to materials
            input_is_intermediate_material: bool = (
                input_name not in self.final_items and
                not input_is_raw_resource
            )
            if input_is_intermediate_material:
                self.__add_value_to_dict(input_dict, self.inter_materials)
            elif input_is_raw_resource:
                self.__add_value_to_dict(input_dict, self.raw_materials)
                pass

            # add the inputs to the items_to_visit list
            if input_dict != 0:
                items_to_visit.append(input_dict)
