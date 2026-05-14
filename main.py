import pygame as p
import UI.seth_click as c
import UI.seth_hover as h
import Elijah.elite_upgrades as e
import Elijah.rock_generation as r
import sys

def main():
    res=(720,720)
    screen = p.display.set_mode(res,p.RESIZABLE)
    rps=int(0)
    counter=int(0)
    running=True
    upgrades=e.get_all_upgrades()
    buildings=e.get_all_buildings()
    while running:
        screen.fill((0,0,0))
        mouse=p.mouse.get_pos()
        for ev in p.event.get():
            if ev.type==p.MOUSEBUTTONDOWN:
                counter=c.click(mouse,upgrades,counter,buildings,button_mult=1)
            if ev.type==p.QUIT:
                running=False
        r.update_rock_generation(rps,upgrades,buildings)
        counter=r.generate_rocks(counter,rps)
        h.hover(mouse,counter,buildings,upgrades)
        p.display.update()

    p.quit()
    sys.exit()

main()