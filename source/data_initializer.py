
# file initializes data from json and checks it over for any logical errors

import os
import json


DATA_DIR: str = "../data/"


# TODO: add a context argument for the "__name__" to be printed, or something.
class BookData():
    def __init__(self):
        print(f"Data directory is set as: '{DATA_DIR}'")

        self.extraction: dict = {}
        self.recipes: dict = {}
        self.machines: dict = {}
        self.resources: dict = {}

        self.book_paths: list[str] = self.__ls_dir_abs(DATA_DIR)
        self.__load_into_dicts(self.__json_load(self.book_paths))
        if self.check_books():
            print("Book Data is fully loaded and verified.")
        else:
            print("Problem found with books.")

    def __ls_dir_abs(self, path: str) -> list[str]:
        directory_files = os.listdir(path)
        directory_files = list(
            map(lambda x: os.path.join(DATA_DIR, x), directory_files))
        directory_files = list(
            map(lambda x: os.path.abspath(x), directory_files))
        return list(
            filter(lambda x: os.path.isfile(x), directory_files))

    def __load_into_dicts(self, books: list[dict]):

        for book in books:
            # print(f"New book to sort: {list(book.keys())[0]}")

            if "extraction" in book:
                self.extraction = book["extraction"]
            elif "recipes" in book:
                self.recipes = book["recipes"]
            elif "machines" in book:
                self.machines = book["machines"]
            elif "resources" in book:
                self.resources = book["resources"]
            else:
                print("""Error, additional dictionary loaded from file.
No dict object ready.""")
                print(f"Please create dict object for: {list(book.keys())[0]}")
                return
        # print("All books were placed in the global variables")

    def __json_load(self, paths: list[str]) -> list[dict]:
        dicts: list[dict] = []
        for path in paths:

            try:
                with open(path, 'r') as data_file:
                    dicts.append(json.load(data_file))

            except FileNotFoundError as e:
                print("File was not found, please check path:",
                      path, e)
            except IOError as e:
                print("Error occured while working with file at path:",
                      path, e)

        return dicts

    def check_books(self) -> bool:
        for book in [self.extraction, self.recipes,
                     self.resources, self.machines]:
            if book == {}:
                print(f"The following book is empty!\n{book}")
                return False
        return True


def main():
    _ = BookData()


if __name__ == "__main__":
    main()
