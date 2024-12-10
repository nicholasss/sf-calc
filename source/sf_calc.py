# core of program
# parses arguments
# calls other modules for calculations and loading

import sys
import argparse

from bookdata import BookData

from search import Search
from recipenode import RecipeNode, IONode
from recipetree import RecipeTree

# setup parser object
parser = argparse.ArgumentParser(description="Satisfactory Calculator CLI.")

# parser arguments
# default argument for what to calculate for
parser.add_argument("recipe", help="What recipe to calculate", nargs="*")
# '-c' optionally supplied for how many to calc
parser.add_argument(
    "-c", "--count", help="How many of a recipe to calculate", metavar="recipe"
)
# list will default to value of "all", if none specified
parser.add_argument(
    "-l", "--list", help="list all possible recipes", nargs="?", const="all"
)
# TODO: how to sort recipes for listing?

# parsing args
args = parser.parse_args()


def __printf(print_dict: dict, cont: str = ""):
    for key in print_dict:
        if key is None:
            continue
        value = print_dict[key]

        if type(value) is int:
            print("> {:5d}".format(value), key, cont)
        elif type(value) is float:
            print("> {:5.1f}".format(value), key, cont)


def main():
    # argv: list[str] = sys.argv
    argc: int = len(sys.argv)

    if argc <= 1:
        print("Not enough arguments provided.")
        return

    # print(f"\nProvided arguments are: {args}")

    # NOTE: List Argument
    if args.list is not None and args.list == "all".lower():
        bd = BookData()  # BookData is only initialized if we need to list
        for recipe in bd.recipes:
            machine = bd.recipes[recipe]["machine"]
            print("-{:15s} made in {:15s}".format(recipe, machine))
        del bd

    if args.count:
        try:
            count = int(args.count)
        except ValueError:
            print("Please supply an integer for count. Setting as 1.")
            count = 1

        if count <= 0:
            print("Count provided needs to be at least 1. Setting as 1.")
            count = 1

    else:  # count was not provided
        count = 1

    # NOTE: Recipe Argument
    if args.recipe:
        # NOTE: testing recipenode class
        rn = RecipeNode(args.recipe[0], count)
        rt = RecipeTree(rn)
        print(rn)
        print(rt)

        if len(args.recipe) > 1:
            print("Too many arguments provided for recipe.")
        recipe = args.recipe[0].title()

        if not args.count:  # count argument was not provided
            bd = BookData()
            count = bd.recipes[recipe]["out"][recipe]
            del bd

        if count > 1:
            s = "s"
        else:
            s = ""
        print(f"Calculating recipe for {count} {recipe}{s}.")

        recipe_request: dict = {recipe: count}

        search = Search()
        search.set_requirements(recipe_request)

        # Printing Request
        print("\nRequested Recipes:")
        __printf(recipe_request, "per min")

        print("\nRaw Materials Needed:")
        __printf(search.raw_materials, "per min")

        print("\nIntermediate Materials to Produce:")
        __printf(search.inter_materials, "per min")

        print("\nMachines Needed For Production:")
        __printf(search.machines_needed)

        print(f"\nTotal Power Requirements: {search.power_mw_needed}MW")

        del search


if __name__ == "__main__":
    main()
