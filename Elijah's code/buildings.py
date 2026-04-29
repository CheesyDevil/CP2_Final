cookies = 0
rps = 0
click_multiplier = 1

from upgrade_logic import math_for_exponential_cost_increase

buildings = [
    {"name": "Pickaxe", "cost": 15, "rps": 0.1, "owned": 0, "mult": 1},
    {"name": "Base Alien", "cost": 100, "rps": 1, "owned": 0, "mult": 1},
    {"name": "Farm", "cost": 1100, "rps": 8, "owned": 0, "mult": 1},
    {"name": "Mine", "cost": 12000, "rps": 47, "owned": 0, "mult": 1},
    {"name": "Factory", "cost": 130000, "rps": 260, "owned": 0, "mult": 1},
    {"name": "Portal", "cost": 10**6, "rps": 10000, "owned": 0, "mult": 1},
    {"name": "Time Machine", "cost": 14 * 10**12, "rps": 65 * 10**6, "owned": 0, "mult": 1}
]

def buy_building(building_index, cookies, rps):
    building = buildings[building_index]
    if cookies >= building["cost"]:
        cookies -= building["cost"]
        building["owned"] += 1
        rps += building["rps"] * building["mult"]
        building["cost"] = math_for_exponential_cost_increase(building["cost"], 1.15, 1)
    return cookies, rps