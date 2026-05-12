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


pickaxe_description = "A sturdy pickaxe that can mine rocks way faster! Increases RPS by 0.1."

alien_description = "A friendly alien that helps you mine rocks! Increases RPS by 1."

grinder_description = "A powerful grinder that can crush rocks into dust for easier processing! Increases RPS by 8."

quarry_description = "A large quarry that can extract rocks from deep in the asteroid's ground! Increases RPS by 47."

rock_factory_description = "A factory that can mass-produce rocks for you! Increases RPS by 260."

asteroid_portal_description = "A portal that allows you to access asteroids in other parts of the universe! Increases RPS by 10,000."

time_machine_description = "Takes you back in time to mine more rocks from the past and future! Increases RPS by 65 million."

quantum_drill_description = "A drill that uses quantum mechanics to mine rocks at an incredible speed, and also be in multiple places at once! Increases RPS by 430 million."

alien_planet_description = "A planet inhabited by friendly aliens who help you mine alien minerals! Increases RPS by 2.9 billion."

dyson_sphere_description = "A megastructure that surrounds a star and captures its energy to mine rocks! Increases RPS by 20 billion."

galaxy_cluster_description = "Now you can mine rocks from multiple different galaxies! Increases RPS by 140 billion."

multiverse_description = "You can now mine rocks from multiple universes at once! Increases RPS by 1 trillion."

buildings = [
    {"name": "Pickaxe", "cost": 15, "rps": 0.1, "owned": False, "mult": 1, "description": pickaxe_description},
    {"name": "Alien", "cost": 100, "rps": 1, "owned": False, "mult": 1, "description": alien_description},
    {"name": "Grinder", "cost": 1100, "rps": 8, "owned": False, "mult": 1, "description": grinder_description},
    {"name": "Quarry", "cost": 12000, "rps": 47, "owned": False, "mult": 1, "description": quarry_description},
    {"name": "Rock Factory", "cost": 130000, "rps": 260, "owned": False, "mult": 1, "description": rock_factory_description},
    {"name": "Asteroid Portal", "cost": 10**6, "rps": 10000, "owned": False, "mult": 1, "description": asteroid_portal_description},
    {"name": "Time Machine", "cost": 14 * 10**12, "rps": 65 * 10**6, "owned": False, "mult": 1, "description": time_machine_description},
    {"name": "Quantum Drill", "cost": 1.4 * 10**15, "rps": 430 * 10**6, "owned": False, "mult": 1, "description": quantum_drill_description},
    {"name": "Alien Planet", "cost": 1.4 * 10**18, "rps": 2.9 * 10**9, "owned": False, "mult": 1, "description": alien_planet_description},
    {"name": "Dyson Sphere", "cost": 1.4 * 10**21, "rps": 20 * 10**9, "owned": False, "mult": 1, "description": dyson_sphere_description},
    {"name": "Galaxy Cluster", "cost": 1.4 * 10**24, "rps": 140 * 10**9, "owned": False, "mult": 1, "description": galaxy_cluster_description},
    {"name": "Multiverse", "cost": 1.4 * 10**27, "rps": 1 * 10**12, "owned": False, "mult": 1, "description": multiverse_description}
]

def buy_building(building_index, cookies, rps):
    building = buildings[building_index]
    if cookies >= building["cost"]:
        cookies -= building["cost"]
        building["owned"] += 1
        rps += building["rps"] * building["mult"]
        building["cost"] = math_for_exponential_cost_increase(building["cost"], 1.15, 1)
    return cookies, rps