# core of program
# parses arguments
# calls other modules for calculations and loading

import sys
import argparse

from data_initializer import (
    DATA_DIR, __ls_dir_abs, __load_json,
    machines, recipes, resources, extraction
)

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

# parsing args
args = parser.parse_args()


def main():
    # argv: list[str] = sys.argv
    argc: int = len(sys.argv)

    if argc <= 1:
        print("Not enough arguments provided.")
        # TODO: help dialog
        return

    # Loading recipes
    data_files: list[str] = __ls_dir_abs(DATA_DIR)
    data_dicts: list[dict] = __load_json(data_files)
    # TODO: dictionaries are not organized at all, should have names
    print(data_dicts)

    print(f"\nProvided arguments are: {args}")

    if args.list is not None:
        print("Listing recipes")


if __name__ == "__main__":
    main()
