import pygame as p

p.init()

res=(720,720)
screen = p.display.set_mode(res)

width=screen.get_width()
height=screen.get_height()

color1=(100,100,100)
color2=(170,170,170)
color3=(0,0,0)
color4=(255,255,255)

desc_font=p.font.SysFont('Corbeal',35)
def hover(mouse,counter, buildings,upgrades):
    #Buildings
    if width/12*7<=mouse[0]<=width/12*11 and height/12*11<=mouse[1]<=height:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*11,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[0].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*10<=mouse[1]<=height/12*11:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*10,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[1].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1])) 
    if width/12*7<=mouse[0]<=width/12*11 and height/12*9<=mouse[1]<=height/12*10:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*9,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[2].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*8<=mouse[1]<=height/12*9:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*8,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[3].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*7<=mouse[1]<=height/12*8:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*7,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[4].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*6<=mouse[1]<=height/12*7:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*6,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[5].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*5<=mouse[1]<=height/12*6:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*5,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[6].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*4<=mouse[1]<=height/12*5:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*4,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[7].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*3<=mouse[1]<=height/12*4:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[8].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*2<=mouse[1]<=height/12*3:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12*2,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[9].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12<=mouse[1]<=height/12*2:
        p.draw.rect(screen,color2,[width/12*7,width/3,height/12,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[10].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and 0<=mouse[1]<=height/12:
        p.draw.rect(screen,color2,[width/12*7,width/3,0,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=buildings[11].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
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
        p.draw.circle(screen,color1,[width/8*3,height/12*5],width/8)
        pass #button_click