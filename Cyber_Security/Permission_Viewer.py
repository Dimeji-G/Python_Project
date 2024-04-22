import os
from datetime import date
import argparse as ag
import stat

class FileScan:
    def __init__(self):
        self.path = ''

    def get_args(self):
        parser = ag.ArgumentParser(description = "Scan all Hidden Hidden Items")
        parser.add_argument("path", help = "Path to folder")

        return parser.parse_args()

    def scan_file(self):
        file_info = os.stat(self.path)
        print("Permission")
        print(stat.filemode(file_info.st_mode))
        print("Timestamps")
        print("Access {0}".format(date.fromtimestamp(file_info.st_atime)))
        print("Modify {0}".format(date.fromtimestamp(file_info.st_mtime)))
        print("Create {0}".format(date.fromtimestamp(file_info.st_ctime)))
        
    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_file()

if __name__ == "__main__":
    walk_instance = FileScan()
    walk_instance.main()
