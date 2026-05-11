import pygame as p
import UI.seth_click as c
import UI.seth_hover as h




def main():
    counter=0
    while True:
        mouse=p.mouse.get_pos()
        for ev in p.event.get():
            if ev.type==p.MOUSEBUTTONDOWN:
                c.click(mouse,upgrades,counter,buildings)
        
        h.hover(mouse,counter,buildings,upgrades)
        p.display.update()

main()