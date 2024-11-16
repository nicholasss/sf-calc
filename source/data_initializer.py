
# file initializes data from json and checks it over for any logical errors

import os
import json
from pathlib import Path


DATA_DIR = "../data/"


def __ls_dir(path: str) -> list[str]:
    directory_files = os.listdir(path)
    # is putting /source/ instead of /data/ into the paths
    directory_files = list(map(lambda x: os.path.abspath(x), directory_files))
    return list(filter(lambda x: not os.path.isfile(x), directory_files))
    # have to reverse, as resolving as true means they are removed


def load_json(paths: list[str]) -> list[dict]:
    dicts: list[dict] = []
    for path in paths:
        with open(path, 'r') as data_file:
            dicts.append(json.loads(data_file))
        print(dicts[-1], indent=4)


def main():
    print("Data directory is set as:", DATA_DIR)
    print("Files listed are:", __ls_dir(DATA_DIR))
    data_list = load_json(__ls_dir(DATA_DIR))


if __name__ == "__main__":
    main()
