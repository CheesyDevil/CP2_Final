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




desc_font=p.font.SysFont('Corbeal',35)
coun_font=p.font.SysFont('Corbeal',40)

def load_image(image,coords,scale):
    oimage=p.image.load(image)
    image=p.transform.scale(oimage,scale)
    screen.blit(image,coords)

def rounding(number):
	length=len(int(number))
	index=(length-1)//3
	letters=["   ",'K  ','M  ','B  ', 'T  ','Qu ','Qi ','Sx ','Sp ','Oc ','Nv ', 'Dc ', 'UnD']
	letter=letters[index]
	fnum=(m.ceil((number*1000)/(10**(length-(length%3)))))/1000
	return f"{fnum} {letter}"


def hover(mouse,counter,buildings,upgrades):
    #Buildings
    for i in range(0,12):
        if width/12*7<=mouse[0]<=width/12*11 and (height/12*(12-(i+1)))<=mouse[1]<=(height/12*(12-i)):
            p.draw.rect(screen,color2,[width/12*7,0,width/3,height/12])
            p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
            text=buildings[i].description
            textbox=desc_font.render(text,True,color4)
            screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    #building upgrades
    for i in range(0,12):
        if width/12*11<=mouse[0]<=width and (height/12*(12-(i+1)))<=mouse[1]<=(height/12*(12-i)):
            p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
            p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
            text=upgrades[i].description
            textbox=desc_font.render(text,True,color4)
            screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    #other upgrades
    for i in range(0,12):
        if 0<=mouse[0]<=width/6 and (height/12*(12-(i+1)))<=mouse[1]<=(height/12*(12-i)):
            p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
            p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
            text=upgrades[i+12].description
            textbox=desc_font.render(text,True,color4)
            screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    #prestige
    if width/6<=mouse[0]<=width/12*7 and height<=mouse[1]<=height/12*11:
        p.draw.rect(screen,color2,[width/6,0,width/12*5,height/12]) #prestige
    #Buildings
    for i in range(0,12):
        p.draw.rect(screen,color1,[width/12*7,height/12*i,width/3,height/12])
    #building upgrades
    for i in range(0,12):
        p.draw.rect(screen,color1,[width/12*11,height/12*i,width/12,height/12]) 
    #other upgrades
    for i in range(0,12):
        p.draw.rect(screen,color1,[0,height/12*i,width/6,height/12])
        #prestige
        p.draw.rect(screen,color1,[width/6,0,width/12*5,height/12])
        #button click
        load_image("asteroid.png",(width/4,height/12*7),(width/4,height/4))
        p.draw.rect(screen,color1,[width/4,height/12*7,width/4,height/4])
        pass #button_click
    #Counter
    c_text=counter
    c_box=coun_font.render(c_text,True,color4)
    screen.blit(c_box,(width/6,height/12*11))
while True:
    p.draw.circle(screen,color1,[width/8*3,height/12*5],width/8)
    p.draw.rect(screen,color1,[width/12*7,0,width/3,height/12])
    p.display.update()