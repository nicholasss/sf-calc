from bookdata import BookData


class IONode:
    def __init__(self, name: str, qty: float):
        self.name: str = name
        self.qty: float = float(qty)

    def __str__(self):
        return f"{self.qty} of {self.name}"

    def __eq__(self, value: object) -> bool:
        if type(value) is IONode:
            return self.name == value.name and self.qty == value.qty
        else:
            return False


class RecipeNode:
    def __init__(self, name: str, qty: float):
        self.name: str = name.title()
        self.type: str = ""
        bd_page = self.__find_in_books()

        # sets qty to output if less than one
        if qty <= 1:
            self.qty = bd_page["out"][self.name]
        else:
            self.qty: float = qty

        self.machine: str = bd_page[
            "machine"
        ]  # does this get converted to the string name? not the page?
        self.power_mw: int = self.__find_power_mw_in_books(self.machine)
        self.inputs: list = []
        self.outputs: list = []

        self.__set_inputs_outputs()

    def __eq__(self, value: object, /) -> bool:
        if type(value) is not RecipeNode:
            return False
        else:
            return (
                self.name == value.name
                and self.qty == value.qty
                and self.machine == value.machine
            )

    def __find_power_mw_in_books(self, machine: str) -> int:
        books = BookData()
        bd_page = 0

        try:
            bd_page = books.machines[machine]
        except KeyError:
            return 0

        return bd_page["power_mw"]

    def __find_in_books(self) -> dict:
        books = BookData()
        bd_page = {}

        try:
            bd_page = books.recipes[self.name]
        except KeyError:
            pass
        if bd_page != {}:
            self.type = "recipe"
            return bd_page

        try:
            bd_page = books.resources[self.name]
        except KeyError:
            print(f"unable to find {self.name} within books")
        if bd_page != {}:
            self.type = "resource"
            return bd_page

    def __set_inputs_outputs(self):
        bd_recipe = self.__find_in_books()
        bd_in = bd_recipe["in"]
        bd_out = bd_recipe["out"]

        if list(bd_out.keys()) == ["self"]:
            # print("Recipe requires no inputs")
            self.inputs.append(None)
            self.outputs.append(IONode("self", bd_out["self"]))

        else:
            for name in bd_in:
                qty = float(bd_in[name])
                self.inputs.append(IONode(name, qty))

            for name in bd_out:
                qty = float(bd_out[name])
                self.outputs.append(IONode(name, qty))

    def __str__(self):
        inputs = []
        for input in self.inputs:
            inputs.append(str(input))

        outputs = []
        for output in self.outputs:
            outputs.append(str(output))

        return f"{self.name}: {self.qty}\n  inputs: {inputs}\n  outputs: {outputs}"
