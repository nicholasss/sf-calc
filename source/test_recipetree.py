import unittest

from recipenode import IONode, RecipeNode
from recipetree import RecipeTree


class TestRecipeTree(unittest.TestCase):
    def test_tree_one(self):
        iron_plate: RecipeNode = RecipeNode("Iron Plate", 20)
        rt1: RecipeTree = RecipeTree(iron_plate)

        self.assertEqual(
            rt1.root,
            iron_plate,
            "Recipe tree name missmatch with root recipe name",
        )
        self.assertEqual(rt1.power_mw, 13, "Incorrect power_mw calculation")
        self.assertEqual(
            [IONode("Iron Ingot", 30)], rt1.inputs, "Intermediate inputs are incorrect"
        )
        self.assertEqual(
            rt1.outputs[0].qty,
            iron_plate.qty,
            "Recipe tree output mismatch with input recipe",
        )
        # print(rt1)

    def test_tree_two(self):
        reinf_iron_plate: RecipeNode = RecipeNode("Reinforced Iron Plate", 5.0)
        rt2: RecipeTree = RecipeTree(reinf_iron_plate)

        self.assertEqual(
            rt2.root,
            reinf_iron_plate,
            "Recipe tree name mismatch with root recipe name",
        )
        self.assertEqual(rt2.power_mw, 45, "Incorrect power_mw calculation")
        self.assertEqual(
            [
                IONode("Screw", 60),
                IONode("Iron Rod", 10),
                IONode("Iron Ingot", 45),
                IONode("Iron Plate", 30),
            ],
            rt2.inputs,
            "Intermediate inputs are incorrect",
        )
        self.assertEqual(
            rt2.outputs[0],
            IONode("Reinforced Iron Plate", 5.0),
            "Recipe tree output mismatch with input recipe",
        )
        # print(rt2)

    def test_tree_three(self):
        # NOTE: testing calcuations of additional qty requested
        double_screws: RecipeNode = RecipeNode("Screw", 80.0)
        rt3: RecipeTree = RecipeTree(double_screws)
        self.assertEqual(
            rt3.root,
            double_screws,
            "Recipe tree root recipe mismatch with original recipe",
        )
        self.assertEqual(
            IONode("Screw", 80.0),
            rt3.outputs[0],
            "Recipe tree output mismatch with root recipe",
        )

        print(rt3)
