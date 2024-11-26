from bookdata import BookData


class RecipeNode():
    def __init__(self, name: str, qty: float):
        bd = BookData()
        bd_recipe = bd.recipes[self.name]

        self.name: str = name
        self.qty: float = qty
        self.machine: str = bd_recipe["machine"]
        self.inputs: list[RecipeNode]
        self.outputs: list[RecipeNode]
        del bd

        self.__set_inputs_outputs()

    def __set_inputs_outputs(self):
        bd = BookData()
        bd_recipe = bd.recipes[self.name]
        bd_in = bd_recipe["in"]
        bd_out = bd_recipe["out"]

        for name in bd_in:
            qty = float(bd_in[name])
            self.inputs.append(RecipeNode(name, qty))

        for name in bd_out:
            qty = float(bd_out[name])
            self.outputs.append(RecipeNode(name, qty))
