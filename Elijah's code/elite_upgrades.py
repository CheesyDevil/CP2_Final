#Upgrades for the Miner Clicker game
import math

def on_click(level):
    click = False

    if click == True:
        return Upgrade("Click Upgrade", 10, 1.5, 0.5)

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

class ClickUpgrade(Upgrade):
    def __init__(self, name, base_cost, cost_multiplier, effect_multiplier):
        super().__init__(name, base_cost, cost_multiplier, effect_multiplier)
