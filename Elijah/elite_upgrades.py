#Upgrades for the Miner Clicker game
#bruh
import math

import csv

from Elijah.upgrade_logic import *

class Upgrade:
    def __init__(self, name, base_cost, cost_multiplier, effect_multiplier, description="",image=""):
        self.name = name
        self.base_cost = base_cost
        self.cost_multiplier = cost_multiplier
        self.effect_multiplier = effect_multiplier
        self.level = 0
        self.description = description
        self.image=image

    def get_cost(self):
        self.base_cost=math.ceil(self.base_cost * (self.cost_multiplier ** self.level))

    def get_effect(self):
        self.effect_multiplier=1 + (self.effect_multiplier * self.level)

    def purchase(self):
        self.level += 1

class Building:
    def __init__(self, name, cost, rps, owned=False, mult=1, description="",image=""):
        self.name = name
        self.cost = cost
        self.rps = rps
        self.owned = owned
        self.mult = mult
        self.description = description
        self.image=image

    def purchase(self,cookies):
        if cookies >= self.cost:
            cookies -= self.cost
            self.owned += 1
            self.cost = math_for_exponential_cost_increase(self.cost, 1.15, 1)

pickaxe_upgrade_description = f"Increases the speed of your Pickaxes!\nIncreases the multiplier for the Pickaxe building by 0.5 for each level of this upgrade\nThe cost of this upgrade doubles with each purchase."

alien_upgrade_description = f"Increases the stamina of your Aliens!\nIncreases the multiplier for the Alien building by 1 for each level of this upgrade\nThe cost of this upgrade increases by 150% with each purchase."

grinder_upgrade_description = f"Make your Grinders sharper!\nIncreases the multiplier for the Grinder building by 2 for each level of this upgrade./nThe cost of this upgrade triples with each purchase."

quarry_upgrade_description = f"Vehicles in your Quarry will now go faster and have more carrying capacity!\nIncreases the multiplier for the Quarry building by 5 for each level of this upgrade.\nThe cost of this upgrade increases by 250% with each purchase."

rock_factory_upgrade_description = f"Your rock factories will now produce more rocks!\nIncreases the multiplier for the Rock Factory building by 10 for each level of this upgrade.\nThe cost of this upgrade quadruples with each purchase."

asteroid_portal_upgrade_description = f"Travel faster through the Asteroid Portal!\nIncreases the multiplier for the Asteroid Portal building by 20 for each level of this upgrade.\nThe cost of this upgrade increases by 350% with each purchase."

time_machine_upgrade_description = f"Your Time Machine will now mine more rocks from the past!\nIncreases the multiplier for the Time Machine building by 50 for each level of this upgrade. \nThe cost of this upgrade quintuples with each purchase."

quantum_drill_upgrade_description = f"Your Quantum Drill will now mine more rocks from the quantum realm! \nIncreases the multiplier for the Quantum Drill building by 100 for each level of this upgrade. \nThe cost of this upgrade increases by 450% with each purchase."

alien_planet_upgrade_description = f"Your Alien Planet will now produce more exotic rocks! \nIncreases the multiplier for the Alien Planet building by 200 for each level of this upgrade. \nThe cost of this upgrade sextuples with each purchase."

dyson_sphere_upgrade_description = f"Your Dyson Sphere will now harness more energy from the stars! \nIncreases the multiplier for the Dyson Sphere building by 500 for each level of this upgrade. \nThe cost of this upgrade increases by 550% with each purchase."

galaxy_cluster_upgrade_description = f"Your Galaxy Cluster will now produce more cosmic dust! \nIncreases the multiplier for the Galaxy Cluster building by 1000 for each level of this upgrade. \nThe cost of this upgrade septuples with each purchase."

multiverse_upgrade_description = f"Your Multiverse will now produce more multiversal energy! \nIncreases the multiplier for the Multiverse building by 2000 for each level of this upgrade. \nThe cost of this upgrade increases by 650% with each purchase."

acid_description = f"Your acid will now dissolve rocks faster! \nIncreases the multiplier for all buildings by 1.5 for each level of this upgrade. \nThe cost of this upgrade doubles with each purchase."

oddly_sharp_shovels_description = f"Your found an ancient shovel that can cut through rocks like butter! \nIncreases the multiplier for all buildings by 1.5 for each level of this upgrade. \nThe cost of this upgrade increases by 150% with each purchase."

pure_luck_description = f"Your miners will now have better luck finding rocks! \nIncreases the multiplier for all buildings by 1 for each level of this upgrade. \nThe cost of this upgrade triples with each purchase."

miners_intuition_description = f"Your miners will now have better intuition about where to find rocks! \nIncreases the multiplier for all buildings by 2 for each level of this upgrade. \nThe cost of this upgrade increases by 250% with each purchase."

get_a_foundry_description = f"You will now have a foundry to process your rocks! \nIncreases the multiplier for all buildings by 5 for each level of this upgrade. \nThe cost of this upgrade increases by 350% with each purchase."

better_tools_description = f"Your tools will now be better quality! \nIncreases the multiplier for all buildings by 10 for each level of this upgrade. \nThe cost of this upgrade increases by 450% with each purchase."

mining_bullets_description = f"Your mining bullets will now be more effective! \nIncreases the multiplier for all buildings by 20 for each level of this upgrade. \nThe cost of this upgrade increases by 550% with each purchase."

asteroid_mining_description = f"You will now be able to mine more asteroids! \nIncreases the multiplier for all buildings by 50 for each level of this upgrade. \nThe cost of this upgrade increases by 650% with each purchase."

massive_dumptruck_description = f"You will now have a massive dump truck to transport your rocks! \nIncreases the multiplier for all buildings by 100 for each level of this upgrade. \nThe cost of this upgrade increases by 750% with each purchase."

alien_technology_description = f"You will now have access to alien technology! \nIncreases the multiplier for all buildings by 200 for each level of this upgrade. \nThe cost of this upgrade increases by 850% with each purchase."

improved_solar_panels_description = f"Your solar panels will now be more efficient and bigger! \nIncreases the multiplier for all buildings by 500 for each level of this upgrade. \nThe cost of this upgrade increases by 950% with each purchase."

insane_aliens_description = f"Your aliens will now be more insane and productive! \nIncreases the multiplier for all buildings by 1000 for each level of this upgrade. \nThe cost of this upgrade increases by 1050% with each purchase."

pickaxe_description = f"A sturdy pickaxe that can mine rocks way faster! Increases RPS by 0.1."

alien_description = f"A friendly alien that helps you mine rocks! Increases RPS by 1."

grinder_description = f"A powerful grinder that can crush rocks into dust for easier processing! Increases RPS by 8."

quarry_description = f"A large quarry that can extract rocks from deep in the asteroid's ground! Increases RPS by 47."

rock_factory_description = f"A factory that can mass-produce rocks for you! Increases RPS by 260."

asteroid_portal_description = f"A portal that allows you to access asteroids in other parts of the universe! Increases RPS by 10,000."

time_machine_description = f"Takes you back in time to mine more rocks from the past and future! Increases RPS by 65 million."

quantum_drill_description = f"A drill that uses quantum mechanics to mine rocks at an incredible speed, and also be in multiple places at once! Increases RPS by 430 million."

alien_planet_description = f"A planet inhabited by friendly aliens who help you mine alien minerals! Increases RPS by 2.9 billion."

dyson_sphere_description = f"A megastructure that surrounds a star and captures its energy to mine rocks! Increases RPS by 20 billion."

galaxy_cluster_description = f"Now you can mine rocks from multiple different galaxies! Increases RPS by 140 billion."

multiverse_description = f"You can now mine rocks from multiple universes at once! Increases RPS by 1 trillion."

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

upgrade_stats = {
    "pickaxe": ("Pickaxe Upgrade", 75, 2, 0.5, pickaxe_upgrade_description),
    "alien": ("Alien Upgrade", 1000, 2.5, 1, alien_upgrade_description),
    "grinder": ("Grinder Upgrade", 11000, 3, 2, grinder_upgrade_description),
    "quarry": ("Massive Mine Upgrade", 120000, 3.5, 5, quarry_upgrade_description),
    "rock_factory": ("Rock Factory Upgrade", 1300000, 4, 10, rock_factory_upgrade_description),
    "asteroid_portal": ("Portal to Asteroid Upgrade", 10**6, 4.5, 20, asteroid_portal_upgrade_description),
    "time_machine": ("Time Machine Upgrade", 14 * 10**12, 5, 50, time_machine_upgrade_description),
    "quantum_drill": ("Quantum Drill Upgrade", 1.4 * 10**15, 5.5, 100, quantum_drill_upgrade_description),
    "alien_planet": ("Alien Planet Upgrade", 1.4 * 10**18, 6, 200, alien_planet_upgrade_description),
    "dyson_sphere": ("Dyson Sphere Upgrade", 1.4 * 10**21, 6.5, 500, dyson_sphere_upgrade_description),
    "galaxy_cluster": ("Galaxy Cluster Upgrade", 1.4 * 10**24, 7, 1000, galaxy_cluster_upgrade_description),
    "multiverse": ("Multiverse Upgrade", 1.4 * 10**27, 7.5, 2000, multiverse_upgrade_description)
}

regular_upgrades = {
    "acid": ("Acid Upgrade", 10**5, 2, 0.5, acid_description),
    "oddly sharp shovels": ("Oddly Sharp Shovels Upgrade", 10**6, 2.5, 0.5, oddly_sharp_shovels_description),
    "pure luck": ("Pure Luck Upgrade", 10**7, 3, 1, pure_luck_description),
    "miner's intuition": ("Miner's Intuition Upgrade", 10**8, 3.5, 2, miners_intuition_description),
    "get a foundry": ("Get a Foundry Upgrade", 10**9, 4, 5, get_a_foundry_description),
    "better tools": ("Better Tools Upgrade", 10**10, 4.5, 10, better_tools_description),
    "mining bullets": ("Mining Bullets Upgrade", 10**11, 5, 20, mining_bullets_description),
    "asteroid mining": ("Asteroid Mining Upgrade", 10**12, 5, 50, asteroid_mining_description),
    "MASSIVE Dumptruck": ("MASSIVE Dumptruck Upgrade", 10**13, 5.5, 100, massive_dumptruck_description),
    "alien technology": ("Alien Technology Upgrade", 10**14, 6, 200, alien_technology_description),
    "improved solar panels": ("Improved Solar Panels Upgrade", 10**15, 6.5, 500, improved_solar_panels_description),
    "insane aliens": ("Insane Aliens Upgrade", 10**16, 7, 1000, insane_aliens_description)
}

def get_upgrade(key):
    if key in upgrade_stats:
        name, base_cost, cost_multiplier, effect_multiplier, description = upgrade_stats[key]
        return [Upgrade(name, base_cost, cost_multiplier, effect_multiplier, description)]
        
    elif key in regular_upgrades:
        name, base_cost, cost_multiplier, effect_multiplier, description = regular_upgrades[key]
        return [Upgrade(name, base_cost, cost_multiplier, effect_multiplier, description)]
        
    else:
        raise ValueError("Invalid upgrade!")

def get_all_upgrades():
    all_upgrades = []
    with open("Elijah/upgrade.csv", "r") as f:
        with open("Elijah/building_upgrades.csv", "r") as f2:
            reader = csv.DictReader(f)
            reader_2 = csv.DictReader(f2)
            for row in reader:
                key = row["Key"]
                if key in upgrade_stats:
                    all_upgrades.append(get_upgrade(key)[0])
                elif key in regular_upgrades:
                    all_upgrades.append(get_upgrade(key)[0])
            for row in reader_2:
                key = row["Key"]
                if key in upgrade_stats:
                    all_upgrades.append(get_upgrade(key)[0])
                elif key in regular_upgrades:
                    all_upgrades.append(get_upgrade(key)[0])
        return all_upgrades
    
def get_all_buildings():
    buildings = []
    with open('Elijah/building.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            row = {k.strip(): v for k, v in row.items() if k is not None}
            
            buildings.append(Building(
                row['name'], 
                float(row['cost']), 
                float(row['rps']), 
                row['owned'].strip() == 'True', 
                float(row['multiplier']), 
                row['description variable']
            ))
    return buildings