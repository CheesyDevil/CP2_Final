import pygame as p
import UI.seth_click as c
import UI.seth_hover as h




def main():
    counter=0
    while True:
        for ev in p.event.get():
            if ev.type==p.MOUSEBUTTONDOWN:
                c.click(mouse,upgrades,counter,buildings)
        
        mouse=p.mouse.get_pos()
        h.hover()
        p.display.update()