
# file initializes data from json and checks it over for any logical errors

import os
import json


DATA_DIR: str = "../data/"

extraction: dict = {}
recipes: dict = {}
machines: dict = {}
resources: dict = {}


def __ls_dir_abs(path: str) -> list[str]:
    directory_files = os.listdir(path)
    directory_files = list(
        map(lambda x: os.path.join(DATA_DIR, x), directory_files))
    directory_files = list(map(lambda x: os.path.abspath(x), directory_files))
    return list(filter(lambda x: os.path.isfile(x), directory_files))


def __load_into_dicts(dicts: list[dict]):
    global extraction, recipes, machines, resources

    for book in dicts:
        if "extraction" in book:
            extraction = book
        elif "recipes" in book:
            recipes = book
        elif "machines" in book:
            machines = book
        elif "resources" in book:
            resources = book
        else:
            print("""Error, additional dictionary loaded from file.
No dict object ready.""")
            print(f"Please create dict object for: {list(book.keys())[0]}")


def __load_json(paths: list[str]) -> list[dict]:
    dicts: list[dict] = []
    for path in paths:

        # check for file existing before opening
        try:
            with open(path, 'r') as data_file:
                dicts.append(json.load(data_file))
                # print(json.dumps(dicts[-1], indent=4))

        except FileNotFoundError as e:
            print("File was not found, please check path:", path, e)
        except IOError as e:
            print("Error occured while working with file at path:", path, e)
        finally:
            # print("Read JSON from file at path:", path)
            continue

    return dicts


def main():
    print("Data directory is set as:", DATA_DIR)
    dicts = __load_json(__ls_dir_abs(DATA_DIR))  # list[dict]
    __load_into_dicts(dicts)


if __name__ == "__main__":
    main()
