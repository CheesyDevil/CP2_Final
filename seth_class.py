class Button:
    def __init__(self,x,y):
        self.x=x
        self.y=y

import pygame as p
import sys

p.init()

res=(720,720)
screen = p.display.set_mode(res)

width=screen.get_width()
height=screen.get_height()

def click(mouse):
    if width/2<=mouse[0]<=width/2+200 and height/2<=mouse[1]<=height/2+60:

