# this will parse toml and return the raw data

import os
from pathlib import Path


class TOMLParser():
    def __init__(self):
        print("Creating TOMLParser object")

        self.file_path: os.path = os.getcwd()
        self.buffer: str = ""
        self.current_line: str = ""

    def __set_path(self, path: os.path):
        pass

    def load_file(self, path: os.path):
        self.__set_path(path)

    def return_dict(self):
        pass

        # temp for implementing the module


def main():
    pass


if __name__ == "__main__":
    main()
