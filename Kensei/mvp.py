import pygame
import sys
import csv
import os
import math

pygame.init()

# Windoww
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Miner Clicker MVP")

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()


rocks = 0
click_power = 1

# simpppppppppp
pickaxe_count = 0
pickaxe_base_cost = 50
pickaxe_cost_multiplier = 1.15

# upgrade
upgrade_level = 0
upgrade_base_cost = 200


save_file = "save.csv"

def save_game():
    with open(save_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["rocks", "pickaxes", "upgrade_level"])
        writer.writerow([rocks, pickaxe_count, upgrade_level])

def load_game():
    global rocks, pickaxe_count, upgrade_level
    if os.path.exists(save_file):
        with open(save_file, "r") as f:
            reader = list(csv.reader(f))
            if len(reader) > 1:
                rocks = float(reader[1][0])
                pickaxe_count = int(reader[1][1])
                upgrade_level = int(reader[1][2])

load_game()



def get_pickaxe_cost():
    return int(pickaxe_base_cost * (pickaxe_cost_multiplier ** pickaxe_count))

def get_upgrade_cost():
    return int(upgrade_base_cost * (2 ** upgrade_level))

def get_total_multiplier():
    return 1 + (upgrade_level * 0.5)

def draw_text(text, x, y, size=font):
    img = size.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

#main
while True:
    screen.fill((30, 30, 40))

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Click circle
            if pygame.Rect(300, 200, 200, 200).collidepoint(mx, my):
                rocks += click_power * get_total_multiplier()

            # Buy pickaxe
            if pygame.Rect(50, 400, 200, 50).collidepoint(mx, my):
                cost = get_pickaxe_cost()
                if rocks >= cost:
                    rocks -= cost
                    pickaxe_count += 1

            # Buy upgrade
            if pygame.Rect(550, 400, 200, 50).collidepoint(mx, my):
                cost = get_upgrade_cost()
                if rocks >= cost:
                    rocks -= cost
                    upgrade_level += 1

    #passive
    rocks += pickaxe_count * 0.1 * get_total_multiplier()

#ui

    # Main click button
    pygame.draw.rect(screen, (70, 130, 180), (300, 200, 200, 200))
    draw_text("MINE", 350, 290, big_font)

    # Rocks count
    draw_text(f"Rocks: {int(rocks)}", 320, 100, big_font)

    # Pickaxe button
    pygame.draw.rect(screen, (100, 200, 100), (50, 400, 200, 50))
    draw_text(f"Pickaxe ({pickaxe_count})", 60, 410)
    draw_text(f"Cost: {get_pickaxe_cost()}", 60, 430)

    # Upgrade button
    pygame.draw.rect(screen, (200, 100, 100), (550, 400, 200, 50))
    draw_text(f"Upgrade Lv {upgrade_level}", 560, 410)
    draw_text(f"Cost: {get_upgrade_cost()}", 560, 430)

    # Multiplier display
    draw_text(f"Multiplier: x{round(get_total_multiplier(),2)}", 300, 150)

    pygame.display.flip()
    clock.tick(60)
import pygame
import sys
import csv
import os
import math

pygame.init()

# Windoww
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Miner Clicker MVP")

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()


rocks = 0
click_power = 1

# simpppppppppp
pickaxe_count = 0
pickaxe_base_cost = 50
pickaxe_cost_multiplier = 1.15

# upgrade
upgrade_level = 0
upgrade_base_cost = 200


save_file = "save.csv"

def save_game():
    with open(save_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["rocks", "pickaxes", "upgrade_level"])
        writer.writerow([rocks, pickaxe_count, upgrade_level])

def load_game():
    global rocks, pickaxe_count, upgrade_level
    if os.path.exists(save_file):
        with open(save_file, "r") as f:
            reader = list(csv.reader(f))
            if len(reader) > 1:
                rocks = float(reader[1][0])
                pickaxe_count = int(reader[1][1])
                upgrade_level = int(reader[1][2])

load_game()



def get_pickaxe_cost():
    return int(pickaxe_base_cost * (pickaxe_cost_multiplier ** pickaxe_count))

def get_upgrade_cost():
    return int(upgrade_base_cost * (2 ** upgrade_level))

def get_total_multiplier():
    return 1 + (upgrade_level * 0.5)

def draw_text(text, x, y, size=font):
    img = size.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

#main
while True:
    screen.fill((30, 30, 40))

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Click circle
            if pygame.Rect(300, 200, 200, 200).collidepoint(mx, my):
                rocks += click_power * get_total_multiplier()

            # Buy pickaxe
            if pygame.Rect(50, 400, 200, 50).collidepoint(mx, my):
                cost = get_pickaxe_cost()
                if rocks >= cost:
                    rocks -= cost
                    pickaxe_count += 1

            # Buy upgrade
            if pygame.Rect(550, 400, 200, 50).collidepoint(mx, my):
                cost = get_upgrade_cost()
                if rocks >= cost:
                    rocks -= cost
                    upgrade_level += 1

    #passive
    rocks += pickaxe_count * 0.1 * get_total_multiplier()

#ui

    # Main click button
    pygame.draw.rect(screen, (70, 130, 180), (300, 200, 200, 200))
    draw_text("MINE", 350, 290, big_font)

    # Rocks count
    draw_text(f"Rocks: {int(rocks)}", 320, 100, big_font)

    # Pickaxe button
    pygame.draw.rect(screen, (100, 200, 100), (50, 400, 200, 50))
    draw_text(f"Pickaxe ({pickaxe_count})", 60, 410)
    draw_text(f"Cost: {get_pickaxe_cost()}", 60, 430)

    # Upgrade button
    pygame.draw.rect(screen, (200, 100, 100), (550, 400, 200, 50))
    draw_text(f"Upgrade Lv {upgrade_level}", 560, 410)
    draw_text(f"Cost: {get_upgrade_cost()}", 560, 430)

    # Multiplier display
    draw_text(f"Multiplier: x{round(get_total_multiplier(),2)}", 300, 150)

    pygame.display.flip()
    clock.tick(60)
