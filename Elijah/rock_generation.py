#EHCP2 automatic rock generation
import time


def generate_rocks(cookies, rps):
    while True:
        time.sleep(.1)
        cookies += rps/10
        return cookies

def start_rock_generation(cookies, rps):
    import multiprocessing
    rock_generation_process = multiprocessing.Process(target=generate_rocks, args=(cookies, rps))
    rock_generation_process.daemon = True
    rock_generation_process.start()

def update_rock_generation(rps, upgrades, buildings):
    for i in buildings:
        rps+=(buildings[i].rps*upgrades[i]*buildings[i].owned)
    for i in range(0,12):
        rps=rps*(1+upgrades[i+12].effect_multiplier)
    return rps