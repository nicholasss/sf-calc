from recipenode import RecipeNode, IONode


class RecipeTree():
    def __init__(self, root_recipe: RecipeNode):
        self.root: RecipeNode = root_recipe

        self.raw_inputs: list = []
        self.inputs: list = []
        self.outputs: list = []

        self.machines: list(str) = []
        self.power_mw: int = 0

        self.__load_inputs()

    def __str__(self):
        return f"Root: {self.root.name}\ninputs: {self.raw_inputs}"

    def __load_inputs(self):
        # for each IONode in the nodes inputs, create a RecipeNode and
        # add its inputs unless its "self"
        to_visit: list = self.root.inputs

        while len(to_visit) > 0:
            curr_io_node: IONode = to_visit.pop()
            if curr_io_node is None:
                continue

            curr_recipe_node: RecipeNode = RecipeNode(
                curr_io_node.name, curr_io_node.qty)

            if curr_recipe_node.type == "recipe":
                self.inputs.append(curr_io_node)
            elif curr_recipe_node.type == "resource":
                self.raw_inputs.append(curr_io_node)

            # add its inputs to the list
            to_visit.extend(curr_recipe_node.inputs)

    def __load_outputs(self):
        pass

        # same as inputs but only for the outputs

    def __load_machines_power_reqs(self):
        pass
