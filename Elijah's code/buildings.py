cookies = 0
rps = 0
click_multiplier = 1

from upgrade_logic import math_for_exponential_cost_increase

buildings = [
    {"name": "Pickaxe", "cost": 15, "rps": 0.1, "owned": False, "mult": 1},
    {"name": "Alien", "cost": 100, "rps": 1, "owned": False, "mult": 1},
    {"name": "Small Mine", "cost": 1100, "rps": 8, "owned": False, "mult": 1},
    {"name": "MASSIVE Mine", "cost": 12000, "rps": 47, "owned": False, "mult": 1},
    {"name": "Rock Factory", "cost": 130000, "rps": 260, "owned": False, "mult": 1},
    {"name": "Portal to Asteroid", "cost": 10**6, "rps": 10000, "owned": False, "mult": 1},
    {"name": "Time Machine", "cost": 14 * 10**12, "rps": 65 * 10**6, "owned": False, "mult": 1},
    {"name": "Quantum Drill", "cost": 1.4 * 10**15, "rps": 430 * 10**6, "owned": False, "mult": 1},
    {"name": "Alien Planet", "cost": 1.4 * 10**18, "rps": 2.9 * 10**9, "owned": False, "mult": 1},
    {"name": "Dyson Sphere", "cost": 1.4 * 10**21, "rps": 20 * 10**9, "owned": False, "mult": 1},
    {"name": "Galaxy Cluster", "cost": 1.4 * 10**24, "rps": 140 * 10**9, "owned": False, "mult": 1},
    {"name": "Multiverse", "cost": 1.4 * 10**27, "rps": 1 * 10**12, "owned": False, "mult": 1}
]

base_building_upgrades = [
    {"name": "Wood Pickaxe", "cost": 100, "target": 0, "req": 1, "bought": False},
    {"name": "Forwards from Aliens", "cost": 1000, "target": 1, "req": 1, "bought": False},
    {"name": "Bigger Equipment for Mines", "cost": 1.3 * 1100, "target": 4, "req": 1, "bought": False}
]

def buy_building(building_index, cookies, rps):
    building = buildings[building_index]
    if cookies >= building["cost"]:
        cookies -= building["cost"]
        building["owned"] += 1
        rps += building["rps"] * building["mult"]
        building["cost"] = math_for_exponential_cost_increase(building["cost"], 1.15, 1)
    return cookies, rps