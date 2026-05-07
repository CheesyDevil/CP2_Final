cookies = 0
rps = 0
click_multiplier = 1

from upgrade_logic import *

class Building:
    def __init__(self, name, cost, rps, owned=False, mult=1, description=""):
        self.name = name
        self.cost = cost
        self.rps = rps
        self.owned = owned
        self.mult = mult
        self.description = description

    def purchase(self):
        if cookies >= self.cost:
            global cookies, rps
            cookies -= self.cost
            self.owned += 1
            rps += self.rps * self.mult
            self.cost = math_for_exponential_cost_increase(self.cost, 1.15, 1)

buildings = [
    {"name": "Pickaxe", "cost": 15, "rps": 0.1, "owned": False, "mult": 1},
    {"name": "Alien", "cost": 100, "rps": 1, "owned": False, "mult": 1},
    {"name": "Grinder", "cost": 1100, "rps": 8, "owned": False, "mult": 1},
    {"name": "Quarry", "cost": 12000, "rps": 47, "owned": False, "mult": 1},
    {"name": "Rock Factory", "cost": 130000, "rps": 260, "owned": False, "mult": 1},
    {"name": "Asteroid Portal", "cost": 10**6, "rps": 10000, "owned": False, "mult": 1},
    {"name": "Time Machine", "cost": 14 * 10**12, "rps": 65 * 10**6, "owned": False, "mult": 1},
    {"name": "Quantum Drill", "cost": 1.4 * 10**15, "rps": 430 * 10**6, "owned": False, "mult": 1},
    {"name": "Alien Planet", "cost": 1.4 * 10**18, "rps": 2.9 * 10**9, "owned": False, "mult": 1},
    {"name": "Dyson Sphere", "cost": 1.4 * 10**21, "rps": 20 * 10**9, "owned": False, "mult": 1},
    {"name": "Galaxy Cluster", "cost": 1.4 * 10**24, "rps": 140 * 10**9, "owned": False, "mult": 1},
    {"name": "Multiverse", "cost": 1.4 * 10**27, "rps": 1 * 10**12, "owned": False, "mult": 1}
]

def buy_building(building_index, cookies, rps):
    building = buildings[building_index]
    if cookies >= building["cost"]:
        cookies -= building["cost"]
        building["owned"] += 1
        rps += building["rps"] * building["mult"]
        building["cost"] = math_for_exponential_cost_increase(building["cost"], 1.15, 1)
    return cookies, rps