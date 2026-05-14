import pygame as p

p.init()

screen = p.display.set_mode((720,720),p.RESIZABLE)





width=screen.get_width()
height=screen.get_height()

def button_click(button_flat,button_mult,counter):
    counter+=button_flat*button_mult
    return counter


button_flat=1
button_mult=1




def click(mouse,upgrades,counter, buildings,button_mult):
    def button_click(button_flat,button_mult,counter):
        counter+=button_flat*button_mult
        return counter
    #Buildings
    for i in range(0,12):
        if width/12*7<=mouse[0]<=width/12*11 and height/12*(12-(i+1))<=mouse[1]<=height/12*(12-i):
            if buildings[11-i].cost<=counter:
                return buildings[11-i].purchase(counter)
    #building upgrades
    for i in range(0,12):
        if width/12*11<=mouse[0]<=width and height/12*(12-(i+1))<=mouse[1]<=height/12*(12-i):
            if upgrades[11-i].base_cost<=counter:
                return upgrades[11-i].purchase(counter)
    #other upgrades
    for i in range(0,12):
        if 0<=mouse[0]<=width/6 and height/12*(12-(i+1))<=mouse[1]<=height/12*(12-i):
            if upgrades[23-i].base_cost<=counter:
                return upgrades[23-i].purchase(counter)
    #prestige
    if width/6<=mouse[0]<=width/12*7 and height<=mouse[1]<=height/12*11:
        pass #prestige
    #button click
    else:
       return button_click(button_flat,button_mult,counter) #button_click