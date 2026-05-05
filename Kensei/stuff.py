import math
from prestige import *


#don't know if we need this
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