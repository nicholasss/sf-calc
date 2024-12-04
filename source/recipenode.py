from bookdata import BookData


class IONode():
    def __init__(self, name: str, qty: float):
        self.name = name
        self.qty = qty

    def __str__(self):
        return f"{self.qty} of {self.name}"


class RecipeNode():
    def __init__(self, name: str, qty: float):
        self.name: str = name.title()
        self.type: str = None
        bd_page = self.__find_in_books()

        # sets qty to output if less than one
        if qty <= 1:
            self.qty = bd_page["out"][self.name]
        else:
            self.qty: float = qty

        self.machine: str = bd_page["machine"]
        self.inputs: list = []
        self.outputs: list = []

        self.__set_inputs_outputs()

    def __find_in_books(self):
        books = BookData()
        bd_page = None

        try:
            bd_page = books.recipes[self.name]
        except KeyError:
            pass
        if bd_page is not None:
            self.type = "recipe"
            return bd_page

        try:
            bd_page = books.resources[self.name]
        except KeyError:
            print(f"unable to find {self.name} within books")
        if bd_page is not None:
            self.type = "resource"
            return bd_page

    def __set_inputs_outputs(self):
        bd_recipe = self.__find_in_books()
        bd_in = bd_recipe["in"]
        bd_out = bd_recipe["out"]

        if list(bd_out.keys()) == ["self"]:
            print("Recipe requires no inputs")
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
