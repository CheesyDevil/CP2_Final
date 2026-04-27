class Text:
    def __init__(self,text, font,font_size, text_color):
        self.text=text
        self.font=font
        self.font_size=font_size
        self.text_color=text_color

class Button:
    def __init__(self,shape,text1,text1_location,text2=False,text2_location=False,text3=False,text3_location=False,image=False,popup=False):
        self.shape=shape
        self.text1=text1
        self.text1_location=text1_location
        self.text2=text2
        self.text2_location=text2_location
        self.text3=text3
        self.text3_location=text3_location
        self.image=image
        self.popup=popup
