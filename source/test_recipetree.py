import unittest

from recipenode import IONode, RecipeNode
from recipetree import RecipeTree


class TestRecipeTree(unittest.TestCase):
    def test_tree_one(self):
        iron_plate: RecipeNode = RecipeNode("Iron Plate", 30)
        rt1: RecipeTree = RecipeTree(iron_plate)

        self.assertEqual(str(rt1.root), str(iron_plate))
        print(rt1)

    def test_tree_two(self):
        reinf_iron_plate: RecipeNode = RecipeNode("Reinforced Iron Plate", 5)
        rt2: RecipeTree = RecipeTree(reinf_iron_plate)

        self.assertEqual(str(rt2.root), str(reinf_iron_plate))
        print(rt2)
