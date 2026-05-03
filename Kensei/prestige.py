#kh
import math


def convert_lifetime_rocks_to_strange_matter(lifetime_rocks):
    #Conversion only happens when the player confirms prestige.
    return math.floor(
        (lifetime_rocks / 1_000_000_000_000) ** (1 / 3)
    )



class PrestigeUpgrade:
    def __init__(self, upgrade_id, display_name, base_cost, cost_growth, effect_per_level):
        self.upgrade_id = upgrade_id          #  identifier
        self.display_name = display_name      # UI name
        self.level = 0
        self.base_cost = base_cost
        self.cost_growth = cost_growth
        self.effect_per_level = effect_per_level

    def cost_for_next_level(self):
        return self.base_cost + (self.level * self.cost_growth)

    def can_afford(self, strange_matter):
        return strange_matter >= self.cost_for_next_level()

    def purchase(self):
        self.level += 1

    def multiplier(self):
        return 1 + (self.level * self.effect_per_level)


class PrestigeShop:
    def __init__(self):
        self.upgrades = {
            "rock_mastery": PrestigeUpgrade(
                upgrade_id="rock_mastery",
                display_name="Rock mastery",
                base_cost=1,
                cost_growth=5,
                effect_per_level=0.25
            ),
            "idle_amplification": PrestigeUpgrade(
                upgrade_id="idle_amplification",
                display_name="Idle amplification",
                base_cost=2,
                cost_growth=6,
                effect_per_level=0.20
            ),
            "matter_efficiency": PrestigeUpgrade(
                upgrade_id="matter_efficiency",
                display_name="Matter efficiency",
                base_cost=5,
                cost_growth=15,
                effect_per_level=0.10
            ),
            "prestige_momentum": PrestigeUpgrade(
                upgrade_id="prestige_momentum",
                display_name="Prestige momentum",
                base_cost=8,
                cost_growth=20,
                effect_per_level=1.0
            ),
            "temporal_compression": PrestigeUpgrade(
                upgrade_id="temporal_compression",
                display_name="Temporal compression",
                base_cost=15,
                cost_growth=35,
                effect_per_level=0.05
            ),
        }

    def purchase_upgrade(self, upgrade_id, strange_matter):
        upgrade = self.upgrades[upgrade_id]

        if not upgrade.can_afford(strange_matter):
            return False, strange_matter

        cost = upgrade.cost_for_next_level()
        upgrade.purchase()
        strange_matter -= cost

        return True, strange_matter


#code game? elijah might made already

class GameState:
    def __init__(self):
        self.current_rocks = 0
        self.base_rocks_per_second = 1

        self.lifetime_rocks = 0
        self.strange_matter = 0

        self.prestige_shop = PrestigeShop()


    def click_rock(self):
        click_multiplier = (
            self.prestige_shop.upgrades["rock_mastery"].multiplier()
        )

        rocks_gained = 1 * click_multiplier
        self.current_rocks += rocks_gained
        self.lifetime_rocks += rocks_gained

        return rocks_gained

    def generate_rocks_over_time(self, delta_time_seconds):
        idle_multiplier = (
            self.prestige_shop.upgrades["idle_amplification"].multiplier()
        )

        time_multiplier = (
            self.prestige_shop.upgrades["temporal_compression"].multiplier()
        )

        effective_time = delta_time_seconds * time_multiplier
        rocks_gained = (
            self.base_rocks_per_second
            * idle_multiplier
            * effective_time
        )

        self.current_rocks += rocks_gained
        self.lifetime_rocks += rocks_gained

        return rocks_gained


    def get_prestige_preview(self):
        raw_strange_matter = convert_lifetime_rocks_to_strange_matter(
            self.lifetime_rocks
        )

        efficiency_multiplier = (
            self.prestige_shop.upgrades["matter_efficiency"].multiplier()
        )

        strange_matter_gained = math.floor(
            raw_strange_matter * efficiency_multiplier
        )

        return {
            "lifetime_rocks": self.lifetime_rocks,
            "strange_matter_gained": strange_matter_gained
        }

    def confirm_prestige(self):
        preview = self.get_prestige_preview()
        strange_matter_gained = preview["strange_matter_gained"]

        if strange_matter_gained <= 0:
            return False

        # apply conversion
        self.strange_matter += strange_matter_gained

        # reset runspecific progress
        self.current_rocks = 0
        self.base_rocks_per_second = 1

        return True