import pygame as p

p.init()

res=(720,720)
screen = p.display.set_mode(res)

width=screen.get_width()
height=screen.get_height()

def hover(mouse,counter, buildings,upgrades):
    #Buildings
    if width/12*7<=mouse[0]<=width/12*11 and height/12*11<=mouse[1]<=height:
        if buildings[0].get_cost()<=counter:
            buildings[0].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*10<=mouse[1]<=height/12*11:
        if buildings[1].get_cost()<=counter:
            buildings[1].purchase()    
    if width/12*7<=mouse[0]<=width/12*11 and height/12*9<=mouse[1]<=height/12*10:
        if buildings[2].get_cost()<=counter:
            buildings[2].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*8<=mouse[1]<=height/12*9:
        if buildings[3].get_cost()<=counter:
            buildings[3].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*7<=mouse[1]<=height/12*8:
        if buildings[4].get_cost()<=counter:
            buildings[4].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*6<=mouse[1]<=height/12*7:
        if buildings[5].get_cost()<=counter:
            buildings[5].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*5<=mouse[1]<=height/12*6:
        if buildings[6].get_cost()<=counter:
            buildings[6].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*4<=mouse[1]<=height/12*5:
        if buildings[7].get_cost()<=counter:
            buildings[7].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*3<=mouse[1]<=height/12*4:
        if buildings[8].get_cost()<=counter:
            buildings[8].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12*2<=mouse[1]<=height/12*3:
        if buildings[9].get_cost()<=counter:
            buildings[9].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and height/12<=mouse[1]<=height/12*2:
        if buildings[10].get_cost()<=counter:
            buildings[10].purchase()
    if width/12*7<=mouse[0]<=width/12*11 and 0<=mouse[1]<=height/12:
        if buildings[11].get_cost()<=counter:
            buildings[11].purchase()
    #building upgrades
    if width/12*11<=mouse[0]<=width and height/12*11<=mouse[1]<=height:
        if upgrades[0].get_cost()<=counter:
            upgrades[0].purchase()
    if width/12*11<=mouse[0]<=width and height/12*10<=mouse[1]<=height/12*11:
        if upgrades[1].get_cost()<=counter:
            upgrades[1].purchase()    
    if width/12*11<=mouse[0]<=width and height/12*9<=mouse[1]<=height/12*10:
        if upgrades[2].get_cost()<=counter:
            upgrades[2].purchase()
    if width/12*11<=mouse[0]<=width and height/12*8<=mouse[1]<=height/12*9:
        if upgrades[3].get_cost()<=counter:
            upgrades[3].purchase()
    if width/12*11<=mouse[0]<=width and height/12*7<=mouse[1]<=height/12*8:
        if upgrades[4].get_cost()<=counter:
            upgrades[4].purchase()
    if width/12*11<=mouse[0]<=width and height/12*6<=mouse[1]<=height/12*7:
        if upgrades[5].get_cost()<=counter:
            upgrades[5].purchase()
    if width/12*11<=mouse[0]<=width and height/12*5<=mouse[1]<=height/12*6:
        if upgrades[6].get_cost()<=counter:
            upgrades[6].purchase()
    if width/12*11<=mouse[0]<=width and height/12*4<=mouse[1]<=height/12*5:
        if upgrades[7].get_cost()<=counter:
            upgrades[7].purchase()
    if width/12*11<=mouse[0]<=width and height/12*3<=mouse[1]<=height/12*4:
        if upgrades[8].get_cost()<=counter:
            upgrades[8].purchase()
    if width/12*11<=mouse[0]<=width and height/12*2<=mouse[1]<=height/12*3:
        if upgrades[9].get_cost()<=counter:
            upgrades[9].purchase()
    if width/12*11<=mouse[0]<=width and height/12<=mouse[1]<=height/12*2:
        if upgrades[10].get_cost()<=counter:
            upgrades[10].purchase()
    if width/12*11<=mouse[0]<=width and 0<=mouse[1]<=height/12:
        if upgrades[11].get_cost()<=counter:
            upgrades[11].purchase()
    #other upgrades
    if 0<=mouse[0]<=width/6 and height/12*11<=mouse[1]<=height:
        if upgrades[0].get_cost()<=counter:
            upgrades[0].purchase()
    if 0<=mouse[0]<=width/6 and height/12*10<=mouse[1]<=height/12*11:
        if upgrades[1].get_cost()<=counter:
            upgrades[1].purchase()    
    if 0<=mouse[0]<=width/6 and height/12*9<=mouse[1]<=height/12*10:
        if upgrades[2].get_cost()<=counter:
            upgrades[2].purchase()
    if 0<=mouse[0]<=width/6 and height/12*8<=mouse[1]<=height/12*9:
        if upgrades[3].get_cost()<=counter:
            upgrades[3].purchase()
    if 0<=mouse[0]<=width/6 and height/12*7<=mouse[1]<=height/12*8:
        if upgrades[4].get_cost()<=counter:
            upgrades[4].purchase()
    if 0<=mouse[0]<=width/6 and height/12*6<=mouse[1]<=height/12*7:
        if upgrades[5].get_cost()<=counter:
            upgrades[5].purchase()
    if 0<=mouse[0]<=width/6 and height/12*5<=mouse[1]<=height/12*6:
        if upgrades[6].get_cost()<=counter:
            upgrades[6].purchase()
    if 0<=mouse[0]<=width/6 and height/12*4<=mouse[1]<=height/12*5:
        if upgrades[7].get_cost()<=counter:
            upgrades[7].purchase()
    if 0<=mouse[0]<=width/6 and height/12*3<=mouse[1]<=height/12*4:
        if upgrades[8].get_cost()<=counter:
            upgrades[8].purchase()
    if 0<=mouse[0]<=width/6 and height/12*2<=mouse[1]<=height/12*3:
        if upgrades[9].get_cost()<=counter:
            upgrades[9].purchase()
    if 0<=mouse[0]<=width/6 and height/12<=mouse[1]<=height/12*2:
        if upgrades[10].get_cost()<=counter:
            upgrades[10].purchase()
    if 0<=mouse[0]<=width/6 and 0<=mouse[1]<=height/12:
        if upgrades[11].get_cost()<=counter:
            upgrades[11].purchase()
    #prestige
    if width/6<=mouse[0]<=width/12*7 and height<=mouse[1]<=height/12*11:
        pass #prestige
    #button click
    else:
    #Buildings
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*11,height/12])
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*10,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*9,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*8,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*7,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*6,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*5,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*4,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12*2,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,height/12,height/12])  
        p.draw.rect(screen,color1,[width/12*7,width/3,0,height/12])  
        #building upgrades
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*11,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*10,height/12]) 
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*9,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*8,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*7,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*6,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*5,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*4,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*3,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12*2,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,height/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,width/12,0,height/12])
        #other upgrades
        p.draw.rect(screen,color1,[0,width/6,height/12*11,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*10,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*9,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*8,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*7,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*6,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*5,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*4,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*3,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12*2,height/12])
        p.draw.rect(screen,color1,[0,width/6,height/12,height/12])
        p.draw.rect(screen,color1,[0,width/6,0,height/12])
        #prestige
        p.draw.rect(screen,color1,[width/6,width/12*5,height/12*11,height/12])
        #button click
        p.draw.circle(screen,color1,())
        pass #button_click