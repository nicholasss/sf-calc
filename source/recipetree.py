from recipenode import RecipeNode, IONode


class RecipeTree:
    def __init__(self, root_recipe: RecipeNode):
        self.root: RecipeNode = root_recipe

        self.raw_inputs: list = []
        self.inputs: list = []
        self.outputs: list = []

        self.machines: list = []
        self.power_mw: int = 0

        self.__load()
        self.__process()

    def __load(self):
        self.__load_inputs()
        self.__load_outputs()
        self.__load_machines_power_reqs()

    def __process(self):
        self.__process_inputs()
        self.__process_inputs("raw")
        self.__process_machines()

    def __str__(self):
        inputs = []
        for input in self.inputs:
            inputs.append(str(input))

        raw_inputs = []
        for rinput in self.raw_inputs:
            raw_inputs.append(str(rinput))

        outputs = []
        for output in self.outputs:
            outputs.append(str(output))

        machines = []
        for machine in self.machines:
            machines.append(str(machine))

        return f"\nRoot: {self.root.name}\nraw inputs: {raw_inputs}\nintermediate inputs:{inputs}\noutputs: {outputs}\nmachines: {machines}\npower_mw: {self.power_mw}"

    def __process_inputs(self, input_type: str = ""):
        if input_type == "raw":
            nodes = self.raw_inputs.copy()
        else:
            nodes = self.inputs.copy()

        processed_nodes: list = []
        for input_n in nodes:
            processed = next(
                (node for node in processed_nodes if node.name == input_n.name), None
            )
            if processed:
                processed.qty += input_n.qty
            else:
                processed_nodes.append(input_n)

        if input_type == "raw":
            self.raw_inputs = processed_nodes
        else:
            self.inputs = processed_nodes

    def __process_machines(self):
        machines: list = self.machines.copy()
        io_machines: list = []
        for mach in machines:
            io_machines.append(IONode(mach, 1))

        processed_machines: list = []
        for io_machine in io_machines:
            processed = next(
                (mach for mach in processed_machines if mach.name == io_machine.name),
                None,
            )
            if processed:  # already in list
                processed.qty += 1
            else:  # not in list yet
                processed_machines.append(io_machine)

        self.machines = processed_machines

    def __load_inputs(self):
        # for each IONode in the nodes inputs, create a RecipeNode and
        # add its inputs unless its "self"
        to_visit: list = self.root.inputs.copy()

        while len(to_visit) > 0:
            curr_io_node: IONode = to_visit.pop()
            if curr_io_node is None:
                continue

            curr_recipe_node: RecipeNode = RecipeNode(
                curr_io_node.name, curr_io_node.qty
            )

            if curr_recipe_node.type == "recipe":
                self.inputs.append(curr_io_node)
            elif curr_recipe_node.type == "resource":
                self.raw_inputs.append(curr_io_node)

            # add its inputs to the list
            to_visit.extend(curr_recipe_node.inputs)

    def __load_outputs(self):
        self.outputs = self.root.outputs

        # same as inputs but only for the outputs

    def __load_machines_power_reqs(self):
        to_visit: list = self.root.inputs.copy()

        while len(to_visit) > 0:
            curr_io_node: IONode = to_visit.pop()
            if curr_io_node is None:
                continue

            curr_recipe_node: RecipeNode = RecipeNode(
                curr_io_node.name, curr_io_node.qty
            )

            self.machines.append(curr_recipe_node.machine)
            self.power_mw += curr_recipe_node.power_mw

            to_visit.extend(curr_recipe_node.inputs)
