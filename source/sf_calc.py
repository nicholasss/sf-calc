# core of program
# parses arguments
# calls other modules for calculations and loading

import sys
import argparse

from data_initializer import BookData
from search import Search

# setup parser object
parser = argparse.ArgumentParser(description="Satisfactory Calculator CLI.")

# parser arguments
# default argument for what to calculate for
parser.add_argument(
    "recipe", help="What recipe to calculate",
    nargs="*")
# '-c' optionally supplied for how many to calc
parser.add_argument(
    "-c", "--count", help="How many of a recipe to calculate",
    metavar="recipe")
# list will default to value of "all", if none specified
parser.add_argument(
    "-l", "--list", help="list all possible recipes",
    nargs="?", const="all")
# TODO: how to sort recipes for listing?

# parsing args
args = parser.parse_args()


def main():
    # argv: list[str] = sys.argv
    argc: int = len(sys.argv)

    if argc <= 1:
        print("Not enough arguments provided.")
        return

    print(f"\nProvided arguments are: {args}")

    # NOTE: List Argument
    if args.list is not None and args.list == "all".lower():
        bd = BookData()  # BookData is only initialized if we need to list
        for recipe in bd.recipes:
            machine = bd.recipes[recipe]["machine"]
            print("-{:15s} made in {:15s}".format(recipe, machine))

    if args.count:
        try:
            count = int(args.count)
        except ValueError:
            print("Please supply an integer for count. Setting as 1.")
            count = 1
    else:
        count = 1
    if count <= 0:
        print("Count provided needs to be at least 1. Setting as 1.")
        count = 1

    # NOTE: Recipe Argument
    if args.recipe:
        if len(args.recipe) > 1:
            print("Too many arguments provided for recipe.")
        recipe = args.recipe[0].title()
        if count > 1 and not None:
            s = "s"
        else:
            s = ""
        print(f"Calculating recipe for {count} {recipe}{s}.")

        recipe_request: dict = {recipe: count}

        search = Search()
        search.set_requirements(recipe_request)

        # Printing Request
        print("\nRequested Recipes:")
        for item in recipe_request:
            print("-{:5d}/min {:15s}".format(recipe_request[item], item))

        print("\nRaw Materials Needed:")
        for raw_mat in search.raw_materials:
            print("-{:5d}/min {:15s}".format(search.raw_materials[raw_mat],
                                             raw_mat))

        print("\nIntermediate Materials to Produce:")
        for inter_mat in search.inter_materials:
            if inter_mat is None:
                pass
            else:
                print("-{:5d}/min {:15s}".format(search.inter_materials[inter_mat],
                                                 inter_mat))

        print("\nMachines Needed For Production:")
        for machine in search.machines_needed:
            print("-{:5d} {:15s}".format(search.machines_needed[machine],
                                         machine))

        print(f"\nTotal Power Requirements: {search.power_mw_needed}MW")


if __name__ == "__main__":
    main()
