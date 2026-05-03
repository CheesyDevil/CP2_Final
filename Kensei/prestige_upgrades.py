#KH prestige upgrades


class PrestigeUpgrade:
    def __init__(self, name, base_cost, cost_growth, effect_per_level):
        self.name = name
        self.level = 0
        self.base_cost = base_cost
        self.cost_growth = cost_growth
        self.effect_per_level = effect_per_level

    def get_cost_for_next_level(self):
        return self.base_cost + (self.level * self.cost_growth)

    def can_purchase(self, strange_matter):
        return strange_matter >= self.get_cost_for_next_level()

    def purchase(self):
        self.level += 1

    def get_multiplier(self):
        return 1 + (self.level * self.effect_per_level)