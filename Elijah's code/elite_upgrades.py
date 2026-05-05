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
    "all_building": ("All Building Upgrade", 1.4 * 10**30, 8, 5000)
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
    "all_building": ("All Building Upgrade Tier 2", 10**19, 8.5, 10000)
}

def get_upgrade(key):
    if key in upgrade_stats:
        name, base_cost, cost_multiplier, effect_multiplier = upgrade_stats[key]
        return [Upgrade(name, base_cost, cost_multiplier, effect_multiplier)]
        
    elif key in tier_2_upgrades:
        name, base_cost, cost_multiplier, effect_multiplier = tier_2_upgrades[key]
        return [Upgrade(name, base_cost, cost_multiplier, effect_multiplier)]
        
    else:
        raise ValueError("Invalid upgrade key")
    
def get_all_upgrades():
    all_upgrades = []
    for key in upgrade_stats:
        all_upgrades.append(get_upgrade(key)[0])
    for key in tier_2_upgrades:
        all_upgrades.append(get_upgrade(key)[0])
    return all_upgrades

def get_cost(upgrade_key):
    if upgrade_key in upgrade_stats:
        upgrade = get_upgrade(upgrade_key)[0]
        return upgrade.get_cost()
    elif upgrade_key in tier_2_upgrades:
        upgrade = get_upgrade(upgrade_key)[0]
        return upgrade.get_cost()
    else:
        raise ValueError("Invalid upgrade key")
    
def purchase_upgrade(upgrade_key, cookies):
    if upgrade_key in upgrade_stats:
        upgrade = get_upgrade(upgrade_key)[0]
        cost = upgrade.get_cost()
        if cookies >= cost:
            cookies -= cost
            upgrade.purchase()
            return cookies, upgrade
        else:
            raise ValueError("Not enough cookies to purchase this upgrade")
    else:
        raise ValueError("Invalid upgrade key")
    
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

click_description = "Increases your mining power! Increases the number of cookies you get per click by 0.5 for each level of this upgrade. The cost of this upgrade increases by 50% with each purchase."

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

all_building_description = "All of your buildings will now produce more rocks in total! Increases the multiplier for all buildings by 5000 for each level of this upgrade. The cost of this upgrade octuples with each purchase."