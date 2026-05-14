import pygame as p
import math as m
p.init()

res=(720,720)
screen = p.display.set_mode(res,p.RESIZABLE)

width=screen.get_width()
height=screen.get_height()

color1=(100,100,100)
color2=(170,170,170)
color3=(0,0,0)
color4=(255,255,255)




desc_font=p.font.SysFont('Corbeal',20)
coun_font=p.font.SysFont('Corbeal',40)

def load_image(image,coords,scale):
    if image:
        oimage=p.image.load(image)
        image=p.transform.scale(oimage,scale)
        screen.blit(image,coords)
    else:
        pass

def rounding(number):
	length=len(str(int(number)))
	index=(length-1)//3
	letters=["   ",'K  ','M  ','B  ', 'T  ','Qu ','Qi ','Sx ','Sp ','Oc ','Nv ', 'Dc ', 'UnD']
	letter=letters[index]
	fnum=(m.ceil((number*1000)/(10**(length-(length%3)))))/1000
	return f"{fnum} {letter}"


def hover(mouse,counter,buildings,upgrades):
    width=screen.get_width()
    height=screen.get_height()
    #prestige
    if width/6<=mouse[0]<=width/12*7 and height<=mouse[1]<=height/12*11:
        p.draw.rect(screen,color2,[width/6,0,width/12*5,height/12]) #prestige
    #Buildings
    for i in range(0,12):
        p.draw.rect(screen,color1,[width/12*7,height/12*(11-i),width/3,height/12])
    #building upgrades
    for i in range(0,12):
        p.draw.rect(screen,color1,[width/12*11,height/12*(11-i),width/12,height/12]) 
    #other upgrades
    for i in range(0,12):
        p.draw.rect(screen,color1,[0,height/12*(11-i),width/6,height/12])
        #prestige
        p.draw.rect(screen,color1,[width/6,0,width/12*5,height/12])
        #button click
        load_image("GUI\pngaaa.com-53237.png",(width/4,height/12*7),(width/4,height/4))
        p.draw.rect(screen,color1,[width/4,height/12*7,width/4,height/4])
        pass #button_click
    #Counter
    rnumber=rounding(counter)
    countbox=desc_font.render(rnumber,True,color4)
    screen.blit(countbox,[width/6,height/12,width/12*5,height/12])
        #Buildings
    for i in range(0,12):
        if width/12*7<=mouse[0]<=width/12*11 and (height/12*(12-(i+1)))<=mouse[1]<=(height/12*(12-i)):
            p.draw.rect(screen,color2,[width/12*7,height/12*(11-i),width/3,height/12])
            p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
            text=f"{buildings[11-i].cost}\n{buildings[11-i].description}"
            textbox=desc_font.render(text,True,color4)
            screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
            load_image(buildings[11-i].image,(width/12*7,height/12*(11-i)),(width/12,height/12))
    #building upgrades
    for i in range(0,12):
        if width/12*11<=mouse[0]<=width and (height/12*(12-(i+1)))<=mouse[1]<=(height/12*(12-i)):
            p.draw.rect(screen,color2,[width/12*11,height/12*(11-i),width/3,height/12])
            p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
            text=upgrades[11-i].description
            textbox=desc_font.render(text,True,color4)
            screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
            load_image(upgrades[11-i].image,(width/12*11,height/12*(11-i)),(width/12,height/12))
    #other upgrades
    for i in range(0,12):
        if 0<=mouse[0]<=width/6 and (height/12*(12-(i+1)))<=mouse[1]<=(height/12*(12-i)):
            p.draw.rect(screen,color2,[0,height/12*(11-i),width/6,height/12])
            p.draw.rect(screen,color3,[mouse[0]+width/4,mouse[1],width/4,height/6])
            text=upgrades[23-i].description
            textbox=desc_font.render(text,True,color4)
            screen.blit(textbox,(mouse[0]+width/4,mouse[1]))
            load_image(upgrades[23-i].image,(0,height/12*(11-i)),(width/12,height/12))