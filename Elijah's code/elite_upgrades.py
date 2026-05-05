#Upgrades for the Miner Clicker game
import math

from buildings import *

class Upgrade:
    def __init__(self, name, base_cost, cost_multiplier, effect_multiplier):
        self.name = name
        self.base_cost = base_cost
        self.cost_multiplier = cost_multiplier
        self.effect_multiplier = effect_multiplier
        self.level = 0

    def get_cost(self):
        return math.ceil(self.base_cost * (self.cost_multiplier ** self.level))

    def get_effect(self):
        return 1 + (self.effect_multiplier * self.level)

    def purchase(self):
        self.level += 1

upgrade_stats = {
    "click": ("Click Upgrade", 10, 1.5, 0.5),
    "pickaxe": ("Pickaxe Upgrade", 100, 2, 0.5),
    "alien": ("Alien Upgrade", 1000, 2.5, 1),
    "small_mine": ("Grinder Upgrade", 11000, 3, 2),
    "massive_mine": ("Massive Mine Upgrade", 120000, 3.5, 5),
    "rock_factory": ("Rock Factory Upgrade", 1300000, 4, 10),
    "asteroid_portal": ("Portal to Asteroid Upgrade", 10**6, 4.5, 20),
    "time_machine": ("Time Machine Upgrade", 14 * 10**12, 5, 50),
    "quantum_drill": ("Quantum Drill Upgrade", 1.4 * 10**15, 5.5, 100),
    "alien_planet": ("Alien Planet Upgrade", 1.4 * 10**18, 6, 200),
    "dyson_sphere": ("Dyson Sphere Upgrade", 1.4 * 10**21, 6.5, 500),
    "galaxy_cluster": ("Galaxy Cluster Upgrade", 1.4 * 10**24, 7, 1000),
    "multiverse": ("Multiverse Upgrade", 1.4 * 10**27, 7.5, 2000),
    "all_building": ("All Building Upgrade", 1.4 * 10**30, 8, 5000),
}

tier_2_upgrades = {
    "click": ("Click Upgrade Tier 2", 10**6, 2, 1),
    "pickaxe": ("Pickaxe Upgrade Tier 2", 10**7, 2.5, 1),
    "alien": ("Alien Upgrade Tier 2", 10**8, 3, 2),
    "small_mine": ("Grinder Upgrade Tier 2", 10**9, 3.5, 5),
    "massive_mine": ("Massive Mine Upgrade Tier 2", 10**10, 4, 10),
    "rock_factory": ("Rock Factory Upgrade Tier 2", 10**11, 4.5, 20),
    "asteroid_portal": ("Portal to Asteroid Upgrade Tier 2", 10**12, 5, 50),
    "time_machine": ("Time Machine Upgrade Tier 2", 10**13, 5.5, 100),
    "quantum_drill": ("Quantum Drill Upgrade Tier 2", 10**14, 6, 200),
    "alien_planet": ("Alien Planet Upgrade Tier 2", 10**15, 6.5, 500),
    "dyson_sphere": ("Dyson Sphere Upgrade Tier 2", 10**16, 7, 1000),
    "galaxy_cluster": ("Galaxy Cluster Upgrade Tier 2", 10**17, 7.5, 2000),
    "multiverse": ("Multiverse Upgrade Tier 2", 10**18, 8, 5000),
}

def get_upgrade(key):
    if key in upgrade_stats:
        return Upgrade(*upgrade_stats[key])
    return None

click_description = "Increases your mining power! Increases the number of cookies you get per click by 0.5 for each level of this upgrade. The cost of this upgrade increases by 50% with each purchase."

pickaxe_description = "Increases the speed of your Pickaxes! Increases the multiplier for the Pickaxe building by 0.5 for each level of this upgrade. The cost of this upgrade doubles with each purchase."

alien_description = "Increases the stamina of your Aliens! Increases the multiplier for the Alien building by 1 for each level of this upgrade. The cost of this upgrade increases by 150% with each purchase."

grinder_description = "Make your Grinders sharper! Increases the multiplier for the Grinder building by 2 for each level of this upgrade. The cost of this upgrade triples with each purchase."

quarry_description = "Vehicles in your Quarry will now go faster and have more carrying capacity! Increases the multiplier for the Quarry building by 5 for each level of this upgrade. The cost of this upgrade increases by 250% with each purchase."

rock_factory_description = "Your rock factories will now produce more rocks! Increases the multiplier for the Rock Factory building by 10 for each level of this upgrade. The cost of this upgrade quadruples with each purchase."

asteroid_portal_description = "Travel faster through the Asteroid Portal! Increases the multiplier for the Asteroid Portal building by 20 for each level of this upgrade. The cost of this upgrade increases by 350% with each purchase."