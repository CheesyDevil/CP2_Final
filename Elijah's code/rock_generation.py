#EHCP2 automatic rock generation
import time

from buildings import *
from elite_upgrades import *

def generate_rocks(cookies, rps):
    while True:
        time.sleep(1)
        cookies += rps

def start_rock_generation(cookies, rps):
    import multiprocessing
    rock_generation_process = multiprocessing.Process(target=generate_rocks, args=(cookies, rps))
    rock_generation_process.daemon = True
    rock_generation_process.start()

def update_rock_generation(cookies, rps, upgrades, buildings):
    pass