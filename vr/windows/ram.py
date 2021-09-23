import os
import time
import datetime

from pathlib import Path


class RAM:
    def __init__(self):
        self.file = self.find_file()
        self.ram = self.read()
        self.date = datetime.date.today()

    def read(self):
        with open(self.file, 'r') as ram:
            ram = ram.readlines()
            lines = len(ram) - 1
            line = ram[lines].strip().split(',')
            ram_dict = {'used': line[2], 'available': line[3]}
        return ram_dict

    def check_date(self):
        if datetime.date.today() != self.date:
            self.file = self.find_file()

    def find_file(self):
        path = Path(r"tools/OHWM")
        file_list = [str(pp) for pp in path.glob("**/*.csv")]
        file = file_list[len(file_list) - 1]
        time.sleep(3)
        return file
