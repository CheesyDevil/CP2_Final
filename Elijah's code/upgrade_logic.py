
import math

from elite_upgrades import *

def math_for_click_upgrade(level):
    return 1 + (0.5 * level)

def math_for_exponential_cost_increase(base_cost, cost_multiplier, level):
    return base_cost * (cost_multiplier ** level) 

def math_for_effect_multiplier(base_effect, effect_multiplier, level):
    return base_effect * (1 + (effect_multiplier * level))

def math_for_linear_cost_increase(base_cost, cost_increase, level):
    return base_cost + (cost_increase * level)

