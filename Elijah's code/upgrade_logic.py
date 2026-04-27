
def math_for_click_upgrade(level):
    return 1 + (0.5 * level)

def math_for_exponential_cost_increase(base_cost, cost_multiplier, level):
    return base_cost * (cost_multiplier ** level)