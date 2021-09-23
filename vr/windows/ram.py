import os
import time
from datetime import datetime, date

from pathlib import Path


class RAM:
    def __init__(self):
        self.day = date.today()
        self.file = self.find_file()
        self.ram = self.read()

    def read(self):
        self.check_date()
        with open(self.file, 'r') as ram:
            ram = ram.readlines()
            lines = len(ram) - 1
            line = ram[lines].strip().split(',')
            ram_dict = {'used': line[2], 'available': line[3]}
        return ram_dict

    def check_date(self):
        day = date.today()
        if day != self.day:
            t = datetime.now().time()
            check_t = datetime.strptime('00::05::30', '%H::%M::%S').time()
            while True:
                if t <= check_t:
                    time.sleep(120)
                else:
                    break
            self.day = day
            self.file = self.find_file()

    def find_file(self):
        path = Path(r"tools/OHWM")
        file_list = [str(pp) for pp in path.glob("**/*.csv")]
        file = file_list[len(file_list) - 1]
        time.sleep(3)
        return file
