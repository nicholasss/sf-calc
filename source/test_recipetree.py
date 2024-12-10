import unittest

from recipenode import IONode, RecipeNode
from recipetree import RecipeTree


class TestRecipeTree(unittest.TestCase):
    def test_tree_one(self):
        iron_plate: RecipeNode = RecipeNode("Iron Plate", 20)
        rt1: RecipeTree = RecipeTree(iron_plate)

        self.assertEqual(
            str(rt1.root),
            str(iron_plate),
            "Recipe tree name missmatch with root recipe name",
        )
        self.assertEqual(
            rt1.root.qty,
            iron_plate.qty,
            "Recipe tree qty mismatch with root recipe qty",
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
        reinf_iron_plate: RecipeNode = RecipeNode("Reinforced Iron Plate", 5)
        rt2: RecipeTree = RecipeTree(reinf_iron_plate)

        self.assertEqual(
            str(rt2.root),
            str(reinf_iron_plate),
            "Recipe tree name mismatch with root recipe name",
        )
        self.assertEqual(
            rt2.root.qty,
            reinf_iron_plate.qty,
            "Recipe tree qty missmatch with root recipe qty",
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
            rt2.outputs[0].qty,
            reinf_iron_plate.qty,
            "Recipe tree output mismatch with input recipe",
        )
        # print(rt2)

    def test_tree_three(self):
        # NOTE: testing calcuations of additional qty requested
        double_screws: RecipeNode = RecipeNode("Screw", 40.0)
        rt3: RecipeTree = RecipeTree(double_screws)
        self.assertEqual(
            rt3.root,
            double_screws,
            "Recipe tree root recipe mismatch with original recipe",
        )

        print(rt3)
