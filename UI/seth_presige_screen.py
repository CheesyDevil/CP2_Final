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

def click_prestige(mouse,prestige_upgrades):
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        prestige_upgrades[0].upgrade()
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        prestige_upgrades[1].upgrade()
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        prestige_upgrades[2].upgrade()
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        prestige_upgrades[3].upgrade()
def hover_prestige(mouse,prestige_upgrades):
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        p.draw.circle(screen,color1,[width/12*4,height/2],width/12)
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=prestige_upgrades[0].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        p.draw.circle(screen,color1,[width/12*6,height/2],width/12)
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=prestige_upgrades[1].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        p.draw.circle(screen,color1,[width/12*8,height/2],width/12)
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=prestige_upgrades[2].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*3<=mouse[0]<=width/12*5 and height/12*5<=mouse[1]<=height/12*7:
        p.draw.circle(screen,color1,[width/12*10,height/2],width/12)
        p.draw.rect(screen,color3,[mouse[0]-width/4,width/4,mouse[1],height/6])
        text=prestige_upgrades[3].description()
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    else:
        p.draw.circle(screen,color1,[width/12*4,height/2],width/12)
        p.draw.circle(screen,color1,[width/12*6,height/2],width/12)
        p.draw.circle(screen,color1,[width/12*8,height/2],width/12)
        p.draw.circle(screen,color1,[width/12*10,height/2],width/12)