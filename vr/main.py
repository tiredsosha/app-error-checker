import logging
import os
import time
import yaml

from vr.image.screen import screenshot
from vr.image.processing import couter
from vr.windows.uptime import get_uptime
from vr.windows.ram import RAM
from vr.entities.settings import Main


logging.basicConfig(
    filename='vr.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)


def main():
    logging.info('VR CHECKER IS STARTED')

    with open("configs/settings.yaml") as settings:
        settings = Main(**yaml.safe_load(settings))

    memory = RAM()

    while True:
        memory.ram = memory.read()

        used = float(memory.ram['used'][:5])
        available = float(memory.ram['available'][:5])

        if used > settings.max_ram:
            [os.system(f'taskill /F /IM {app}') for app in settings.apps]

        os_uptime = get_uptime()

        logging.debug(
            f'    total ram w/o swap is {used + available} GB'
        )
        logging.debug(
            f'    used ram ram w/o swap is {used} GB'
        )
        logging.debug(
            f'    available ram w/o swap is {available} GB'
        )
        logging.debug(
            f'    os uptime is {os_uptime}'
        )

        screenshot()
        matches = couter(settings.error_name)
        if len(matches) > 0:
            logging.debug(f'   list of errors % is {matches}')
            logging.critical(
                '  error is found. game and oculus app were killed\n')
            [os.system(f'taskill /F /IM {app}') for app in settings.apps]

        else:
            logging.debug(f'   list of errors % is {matches}')

        logging.info(f"   Cycle've ended\n")

        time.sleep(settings.delay)


main()
