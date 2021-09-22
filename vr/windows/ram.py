import os
import time

from pathlib import Path


class RAM:
    def __init__(self):
        self.file = self.find_file()
        self.ram = self.read()

    def read(self):
        with open(self.file, 'r') as ram:
            ram = ram.readlines()
            lines = len(ram) - 1
            line = ram[lines].strip().split(',')
            ram_dict = {'used': line[2], 'available': line[3]}
        return ram_dict

    def delete_prev_files(self):
        #os.system('taskkill /f /im OpenHardwareMonitor.exe')
        #os.system('del /S \OpenHardwareMonitorLog*.csv')
        # time.sleep(20)
        pass

    def find_file(self):
        self.delete_prev_files()
        path = Path(r"tools/OHWM")
        file_list = [str(pp) for pp in path.glob("**/*.csv")]
        [x for x in os.listdir('.') if x.endswith('.csv')]
        file_list = file_list[0]
        time.sleep(3)
        return file_list
