from bookdata import BookData


class RecipeNode():
    def __init__(self, name: str, qty: float):
        self.name: str = name.title()
        bd_page = self.__find_in_books()

        self.qty: float = qty
        self.machine: str = bd_page["machine"]
        self.inputs: list[RecipeNode] = []
        self.outputs: list[RecipeNode] = []

        self.__set_inputs_outputs()

    def __find_in_books(self):
        books = BookData()
        bd_page = None

        try:
            bd_page = books.recipes[self.name]
        except KeyError:
            pass
        if bd_page is not None:
            return bd_page

        try:
            bd_page = books.resources[self.name]
        except KeyError:
            print(f"unable to find {self.name} within books")
        if bd_page is not None:
            return bd_page

    def __set_inputs_outputs(self):
        bd_recipe = self.__find_in_books()
        bd_in = bd_recipe["in"]
        bd_out = bd_recipe["out"]

        if bd_in == 0:
            return

        if bd_in != 0:
            for name in bd_in:
                qty = float(bd_in[name])
                self.inputs.append(RecipeNode(name, qty))

            for name in bd_out:
                qty = float(bd_out[name])
                self.outputs.append(RecipeNode(name, qty))

    def __str__(self):
        return f"{self.name}: {self.qty}\n  in:{self.inputs}\n  out:{self.outputs}"
