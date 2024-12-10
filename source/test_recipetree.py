import unittest

from recipenode import IONode, RecipeNode
from recipetree import RecipeTree


class TestRecipeTree(unittest.TestCase):
    def test_tree_one(self):
        iron_plate: RecipeNode = RecipeNode("Iron Plate", 20)
        rt1: RecipeTree = RecipeTree(iron_plate)

        self.assertEqual(str(rt1.root), str(iron_plate))
        self.assertEqual(rt1.root.qty, iron_plate.qty)
        self.assertEqual(rt1.power_mw, 13)
        self.assertEqual([IONode("Iron Ingot", 30)], rt1.inputs)
        print(rt1)

    def test_tree_two(self):
        reinf_iron_plate: RecipeNode = RecipeNode("Reinforced Iron Plate", 5)
        rt2: RecipeTree = RecipeTree(reinf_iron_plate)

        self.assertEqual(str(rt2.root), str(reinf_iron_plate))
        self.assertEqual(rt2.root.qty, reinf_iron_plate.qty)
        self.assertEqual(rt2.power_mw, 45)
        self.assertEqual(
            [
                IONode("Screw", 60),
                IONode("Iron Rod", 10),
                IONode("Iron Ingot", 45),
                IONode("Iron Plate", 30),
            ],
            rt2.inputs,
        )
        print(rt2)
