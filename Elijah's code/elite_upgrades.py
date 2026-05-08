#Upgrades for the Miner Clicker game
import math

from buildings import *

class Upgrade:
    def __init__(self, name, base_cost, cost_multiplier, effect_multiplier, description=""):
        self.name = name
        self.base_cost = base_cost
        self.cost_multiplier = cost_multiplier
        self.effect_multiplier = effect_multiplier
        self.level = 0
        self.description = description

    def get_cost(self):
        return math.ceil(self.base_cost * (self.cost_multiplier ** self.level))

    def get_effect(self):
        return 1 + (self.effect_multiplier * self.level)

    def purchase(self):
        self.level += 1

pickaxe_description = "Increases the speed of your Pickaxes! Increases the multiplier for the Pickaxe building by 0.5 for each level of this upgrade. The cost of this upgrade doubles with each purchase."

alien_description = "Increases the stamina of your Aliens! Increases the multiplier for the Alien building by 1 for each level of this upgrade. The cost of this upgrade increases by 150% with each purchase."

grinder_description = "Make your Grinders sharper! Increases the multiplier for the Grinder building by 2 for each level of this upgrade. The cost of this upgrade triples with each purchase."

quarry_description = "Vehicles in your Quarry will now go faster and have more carrying capacity! Increases the multiplier for the Quarry building by 5 for each level of this upgrade. The cost of this upgrade increases by 250% with each purchase."

rock_factory_description = "Your rock factories will now produce more rocks! Increases the multiplier for the Rock Factory building by 10 for each level of this upgrade. The cost of this upgrade quadruples with each purchase."

asteroid_portal_description = "Travel faster through the Asteroid Portal! Increases the multiplier for the Asteroid Portal building by 20 for each level of this upgrade. The cost of this upgrade increases by 350% with each purchase."

time_machine_description = "Your Time Machine will now mine more rocks from the past! Increases the multiplier for the Time Machine building by 50 for each level of this upgrade. The cost of this upgrade quintuples with each purchase."

quantum_drill_description = "Your Quantum Drill will now mine more rocks from the quantum realm! Increases the multiplier for the Quantum Drill building by 100 for each level of this upgrade. The cost of this upgrade increases by 450% with each purchase."

alien_planet_description = "Your Alien Planet will now produce more exotic rocks! Increases the multiplier for the Alien Planet building by 200 for each level of this upgrade. The cost of this upgrade sextuples with each purchase."

dyson_sphere_description = "Your Dyson Sphere will now harness more energy from the stars! Increases the multiplier for the Dyson Sphere building by 500 for each level of this upgrade. The cost of this upgrade increases by 550% with each purchase."

galaxy_cluster_description = "Your Galaxy Cluster will now produce more cosmic dust! Increases the multiplier for the Galaxy Cluster building by 1000 for each level of this upgrade. The cost of this upgrade septuples with each purchase."

multiverse_description = "Your Multiverse will now produce more multiversal energy! Increases the multiplier for the Multiverse building by 2000 for each level of this upgrade. The cost of this upgrade increases by 650% with each purchase."

acid_description = "Your acid will now dissolve rocks faster! Increases the multiplier for all buildings by 1.5 for each level of this upgrade. The cost of this upgrade doubles with each purchase."

oddly_sharp_shovels_description = "Your found an ancient shovel that can cut through rocks like butter! Increases the multiplier for all buildings by 1.5 for each level of this upgrade. The cost of this upgrade increases by 150% with each purchase."

pure_luck_description = "Your miners will now have better luck finding rocks! Increases the multiplier for all buildings by 1 for each level of this upgrade. The cost of this upgrade triples with each purchase."

miners_intuition_description = "Your miners will now have better intuition about where to find rocks! Increases the multiplier for all buildings by 2 for each level of this upgrade. The cost of this upgrade increases by 250% with each purchase."

get_a_foundry_description = "You will now have a foundry to process your rocks! Increases the multiplier for all buildings by 5 for each level of this upgrade. The cost of this upgrade increases by 350% with each purchase."

better_tools_description = "Your tools will now be better quality! Increases the multiplier for all buildings by 10 for each level of this upgrade. The cost of this upgrade increases by 450% with each purchase."

mining_bullets_description = "Your mining bullets will now be more effective! Increases the multiplier for all buildings by 20 for each level of this upgrade. The cost of this upgrade increases by 550% with each purchase."

asteroid_mining_description = "You will now be able to mine more asteroids! Increases the multiplier for all buildings by 50 for each level of this upgrade. The cost of this upgrade increases by 650% with each purchase."

massive_dumptruck_description = "You will now have a massive dump truck to transport your rocks! Increases the multiplier for all buildings by 100 for each level of this upgrade. The cost of this upgrade increases by 750% with each purchase."

alien_technology_description = "You will now have access to alien technology! Increases the multiplier for all buildings by 200 for each level of this upgrade. The cost of this upgrade increases by 850% with each purchase."

improved_solar_panels_description = "Your solar panels will now be more efficient and bigger! Increases the multiplier for all buildings by 500 for each level of this upgrade. The cost of this upgrade increases by 950% with each purchase."

insane_aliens_description = "Your aliens will now be more insane and productive! Increases the multiplier for all buildings by 1000 for each level of this upgrade. The cost of this upgrade increases by 1050% with each purchase."

upgrade_stats = {
    "pickaxe": ("Pickaxe Upgrade", 75, 2, 0.5, pickaxe_description),
    "alien": ("Alien Upgrade", 1000, 2.5, 1, alien_description),
    "grinder": ("Grinder Upgrade", 11000, 3, 2, grinder_description),
    "quarry": ("Massive Mine Upgrade", 120000, 3.5, 5, quarry_description),
    "rock_factory": ("Rock Factory Upgrade", 1300000, 4, 10, rock_factory_description),
    "asteroid_portal": ("Portal to Asteroid Upgrade", 10**6, 4.5, 20, asteroid_portal_description),
    "time_machine": ("Time Machine Upgrade", 14 * 10**12, 5, 50, time_machine_description),
    "quantum_drill": ("Quantum Drill Upgrade", 1.4 * 10**15, 5.5, 100, quantum_drill_description),
    "alien_planet": ("Alien Planet Upgrade", 1.4 * 10**18, 6, 200, alien_planet_description),
    "dyson_sphere": ("Dyson Sphere Upgrade", 1.4 * 10**21, 6.5, 500, dyson_sphere_description),
    "galaxy_cluster": ("Galaxy Cluster Upgrade", 1.4 * 10**24, 7, 1000, galaxy_cluster_description),
    "multiverse": ("Multiverse Upgrade", 1.4 * 10**27, 7.5, 2000, multiverse_description)
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
    for key in upgrade_
def purchase_upgrade(upgrade_key, cookies):
    if upgrade_key in upgrade_stats:
        upgrade = get_upgrade(upgrade_key)[0]
        cost = upgrade.get_cost()
        if cookies >= cost:
            cookies -= cost
            upgrade.purchase()
            return cookies, upgrade
        else:
            raise ValueError("Not enough rocks to purchase this upgrade")
    else:
        raise ValueError("Invalid upgrade!")
    
def get_effect():
    total_effect = 1
    for upgrade_key in upgrade_stats:
        upgrade = get_upgrade(upgrade_key)[0]
        total_effect *= upgrade.get_effect()
    return total_effect

def upgrade_building(building_index, upgrade_key):
    if upgrade_key in upgrade_stats:
        upgrade = get_upgrade(upgrade_key)
        building = buildings[building_index]
        building["mult"] += upgrade.get_effect()
        upgrade.purchase_upgrade()