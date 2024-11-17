
# file initializes data from json and checks it over for any logical errors

import os
import json


DATA_DIR = "../data/"


def __ls_dir(path: str) -> list[str]:
    directory_files = os.listdir(path)
    directory_files = list(
        map(lambda x: os.path.join(DATA_DIR, x), directory_files))
    directory_files = list(map(lambda x: os.path.abspath(x), directory_files))
    return list(filter(lambda x: os.path.isfile(x), directory_files))


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
            print("Read JSON from file at path:", path)

    return dicts


def main():
    print("Data directory is set as:", DATA_DIR)
    _ = __load_json(__ls_dir(DATA_DIR))  # list[dict]


if __name__ == "__main__":
    main()
