#EHCP2 automatic rock generation
import time

def generate_rocks(cookies, rps):
    while True:
        time.sleep(.1)
        cookies += rps/10
        return cookies

def update_rock_generation(rps, upgrades, buildings):
    for i in range(0,12):
        rps+=(buildings[i].rps*(1+upgrades[i].effect_multiplier)*buildings[i].owned)
    for i in range(0,12):
        rps=rps*(1+upgrades[i+12].effect_multiplier)
    return rps