import unittest

from recipenode import IONode, RecipeNode


class TestIONode(unittest.TestCase):
    def test_one(self):
        ionode1: IONode = IONode("Screw", 40)
        print_ionode1 = "40.0 of Screw"
        self.assertEqual(ionode1.name, "Screw")
        self.assertEqual(ionode1.qty, 40.0)
        self.assertEqual(str(ionode1), print_ionode1)

    def test_two(self):
        ionode2: IONode = IONode("Iron Ingot", 50)
        print_ionode2 = "50.0 of Iron Ingot"
        self.assertEqual(ionode2.name, "Iron Ingot")
        self.assertEqual(ionode2.qty, 50.0)
        self.assertEqual(str(ionode2), print_ionode2)


class TestRecipeNode(unittest.TestCase):
    def test_one(self):
        rcnode1: RecipeNode = RecipeNode("Screw", 40)

        self.assertEqual(rcnode1.name, "Screw")
        self.assertEqual(rcnode1.qty, 40.0)
        self.assertEqual(str(rcnode1.inputs[0]), str(IONode("Iron Rod", 10)))

    def test_two(self):
        rcnode2: RecipeNode = RecipeNode("Iron Ingot", 50)

        self.assertEqual(rcnode2.name, "Iron Ingot")
        self.assertEqual(rcnode2.qty, 50.0)
        self.assertEqual(str(rcnode2.inputs[0]), str(IONode("Iron Ore", 30)))
