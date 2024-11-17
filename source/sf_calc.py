# core of program
# parses arguments
# calls other modules for calculations and loading

import sys
import argparse

from data_initializer import BookData

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

    bd = BookData()

    print(f"\nProvided arguments are: {args}")

    if args.list is not None and args.list == "all".lower():
        print("Listing recipes.")
        for book in bd.recipes:
            name = bd.recipes[book]["name"]
            machine = bd.recipes[book]["machine"]
            print(f"-{name} ({machine})")


if __name__ == "__main__":
    main()
