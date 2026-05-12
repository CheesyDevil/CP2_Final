import pygame as p
import UI.seth_click as c
import UI.seth_hover as h
import Elijah.elite_upgrades as e
import Elijah.rock_generation as r


def main():
    res=(720,720)
    screen = p.display.set_mode(res,p.RESIZABLE)

    rps=0
    counter=0
    while True:
        upgrades=e.get_all_upgrades()
        buildings=e.get_all_buildings()
        mouse=p.mouse.get_pos()
        for ev in p.event.get():
            if ev.type==p.MOUSEBUTTONDOWN:
                c.click(mouse,upgrades,counter,buildings,button_mult=1)
        
        h.hover(mouse,counter,buildings,upgrades)
        r.update_rock_generation(rps,upgrades,buildings)
        counter=r.generate_rocks(counter,rps)
        p.display.update()


main()