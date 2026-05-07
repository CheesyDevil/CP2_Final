import pygame as p

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



def hover(mouse,counter,buildings,upgrades):
    #Buildings
    if width/12*7<=mouse[0]<=width/12*11 and height/12*11<=mouse[1]<=height:
        p.draw.rect(screen,color2,[width/12*7,0,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[0].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*10<=mouse[1]<=height/12*11:
        p.draw.rect(screen,color2,[width/12*7,height/12,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[1].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1])) 
    if width/12*7<=mouse[0]<=width/12*11 and height/12*9<=mouse[1]<=height/12*10:
        p.draw.rect(screen,color2,[width/12*7,height/12*2,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[2].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*8<=mouse[1]<=height/12*9:
        p.draw.rect(screen,color2,[width/12*7,height/12*3,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[3].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*7<=mouse[1]<=height/12*8:
        p.draw.rect(screen,color2,[width/12*7,height/12*4,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[4].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*6<=mouse[1]<=height/12*7:
        p.draw.rect(screen,color2,[width/12*7,height/12*5,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[5].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*5<=mouse[1]<=height/12*6:
        p.draw.rect(screen,color2,[width/12*7,height/12*6,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[6].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*4<=mouse[1]<=height/12*5:
        p.draw.rect(screen,color2,[width/12*7,height/12*7,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[7].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*3<=mouse[1]<=height/12*4:
        p.draw.rect(screen,color2,[width/12*7,height/12*8,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[8].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12*2<=mouse[1]<=height/12*3:
        p.draw.rect(screen,color2,[width/12*7,height/12*9,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[9].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and height/12<=mouse[1]<=height/12*2:
        p.draw.rect(screen,color2,[width/12*7,height/12*10,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[10].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*7<=mouse[0]<=width/12*11 and 0<=mouse[1]<=height/12:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=buildings[11].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    #building upgrades
    if width/12*11<=mouse[0]<=width and height/12*11<=mouse[1]<=height:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[0].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*10<=mouse[1]<=height/12*11:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[1].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*9<=mouse[1]<=height/12*10:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[2].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*8<=mouse[1]<=height/12*9:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[3].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*7<=mouse[1]<=height/12*8:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[4].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*6<=mouse[1]<=height/12*7:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[5].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*5<=mouse[1]<=height/12*6:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[6].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*4<=mouse[1]<=height/12*5:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[7].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*3<=mouse[1]<=height/12*4:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[8].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12*2<=mouse[1]<=height/12*3:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[9].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and height/12<=mouse[1]<=height/12*2:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[10].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if width/12*11<=mouse[0]<=width and 0<=mouse[1]<=height/12:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[11].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    #other upgrades
    if 0<=mouse[0]<=width/6 and height/12*11<=mouse[1]<=height:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[12].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*10<=mouse[1]<=height/12*11:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[13].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*9<=mouse[1]<=height/12*10:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[14].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*8<=mouse[1]<=height/12*9:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[15].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*7<=mouse[1]<=height/12*8:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[16].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*6<=mouse[1]<=height/12*7:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[17].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*5<=mouse[1]<=height/12*6:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[18].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*4<=mouse[1]<=height/12*5:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[19].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*3<=mouse[1]<=height/12*4:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[20].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12*2<=mouse[1]<=height/12*3:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[21].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and height/12<=mouse[1]<=height/12*2:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[22].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    if 0<=mouse[0]<=width/6 and 0<=mouse[1]<=height/12:
        p.draw.rect(screen,color2,[width/12*7,height/12*11,width/3,height/12])
        p.draw.rect(screen,color3,[mouse[0]-width/4,mouse[1],width/4,height/6])
        text=upgrades[23].description
        textbox=desc_font.render(text,True,color4)
        screen.blit(textbox,(mouse[0]-width/4,mouse[1]))
    #prestige
    if width/6<=mouse[0]<=width/12*7 and height<=mouse[1]<=height/12*11:
        pass #prestige
    #button click
    else:
    #Buildings
        p.draw.rect(screen,color1,[width/12*7,0,width/3,height/12])
        p.draw.rect(screen,color1,[width/12*7,height/12,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*2,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*3,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*4,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*5,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*6,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*7,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*8,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*9,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*10,width/3,height/12])  
        p.draw.rect(screen,color1,[width/12*7,height/12*11,width/3,height/12])  
        #building upgrades
        p.draw.rect(screen,color1,[width/12*11,0,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12,width/12,height/12]) 
        p.draw.rect(screen,color1,[width/12*11,height/12*2,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*3,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*4,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*5,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*6,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*7,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*8,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*9,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*10,width/12,height/12])
        p.draw.rect(screen,color1,[width/12*11,height/12*11,width/12,height/12])
        #other upgrades
        p.draw.rect(screen,color1,[0,0,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*2,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*3,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*4,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*5,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*6,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*7,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*8,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*9,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*10,width/6,height/12])
        p.draw.rect(screen,color1,[0,height/12*11,width/6,height/12])
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