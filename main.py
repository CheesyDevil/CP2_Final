import pygame as p
import UI.seth_click as c





def main():
    for ev in p.event.get():
        if ev.type==p.QUIT:
            p.quit()
        if ev.type==p.MOUSEBUTTONDOWN:
            c.click(mouse,upgrades,counter,buildings)
    mouse=p.mouse.get_pos()
    p.display.update()