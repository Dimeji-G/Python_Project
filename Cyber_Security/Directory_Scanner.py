import os
import argparse as ag

class DirectoryWalk():
    def __init__(self):
        self.path = ''

    def get_args(self):
        parser = ag.ArgumentParser(description = "Scan all Hidden Hidden Items")
        parser.add_argument("path", help = "Path to folder")

        return parser.parse_args()

    def scan_path(self):
        with os.scandir(self.path) as item_path:
            for entry in item_path:
                print (entry.name)
                

    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_path()

if __name__ == "__main__":
    walk_instance = DirectoryWalk()
    walk_instance.main()
