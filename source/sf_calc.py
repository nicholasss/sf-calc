# core of program
# parses arguments
# calls other modules for calculations and loading

import sys
import argparse

from bookdata import BookData

from recipenode import RecipeNode
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
            print("-{:23s} made in {:15s}".format(recipe, machine))
        del bd

    if args.count:
        try:
            count = int(args.count)
        except ValueError:
            print("Please supply an integer for count.")
            count = 1

        if count <= 0:
            print("Count provided needs to be at least 1.")
            count = 1

    else:  # count was not provided
        count = 1

    # NOTE: Recipe Argument
    if args.recipe:
        # NOTE: testing recipenode class
        rn = RecipeNode(args.recipe[0], count)
        rt = RecipeTree(rn)

        # Printing Request
        print("\nRequested Recipes:")
        print(rn.qty, rn.name, "per min")

        print("\nRaw Materials Needed:")
        raw_inputs: list = []
        for ri in rt.raw_inputs:
            raw_inputs.append(str(ri))
        raw_inputs_s: str = " per min \n".join(raw_inputs)
        print(raw_inputs_s, "per min")

        print("\nIntermediate Materials to Produce:")
        inter_inputs: list = []
        for ii in rt.inputs:
            inter_inputs.append(str(ii))
        inter_inputs_s: str = " per min\n".join(inter_inputs)
        print(inter_inputs_s, "per min")

        print("\nMachines Needed For Production:")
        machines: list = []
        for mach in rt.machines:
            machines.append(str(mach))
        machines_s: str = " per min\n".join(machines)
        print(machines_s)

        print(f"\nMaximum Power Required: {rt.power_mw}MW")


if __name__ == "__main__":
    main()
