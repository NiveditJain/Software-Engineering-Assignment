import requests
import json
from PIL import Image, ImageDraw, ImageFont

# Class to generate Reciept
class GenerateReciept():
    
    # constructor for Class
    def __init__(self,reciept_number):
        self.reciept_number=reciept_number
        self.request_link="https://niveditjain.github.io/reciept/"+reciept_number+".json"
        self.response=json.loads(requests.get(self.request_link).text)

    def export(self):

        # making imahe and text color settings
        im=Image.open('template.jpg')
        d=ImageDraw.Draw(im)
        text_color = (0, 0, 0)

        # writing reciept number
        font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arialbd.ttf", 40)
        d.text((537, 121), self.response["reciept_number"], fill = text_color, font = font)

        # writing all other details
        font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arialbd.ttf", 30)
        d.text((154, 163), self.response["name"], fill = text_color, font = font)
        d.text((286, 233), self.response["designation"], fill = text_color, font = font)
        d.text((94, 304), self.response["id"], fill = text_color, font = font)
        d.text((187, 375), self.response["status"], fill = text_color, font = font)
        d.text((416, 443), self.response["requested"], fill = text_color, font = font)
        d.text((290, 512), self.response["paid"], fill = text_color, font = font)
        d.text((312, 579), self.response["balance left"], fill = text_color, font = font)
        d.text((27, 756), self.response["signatures"], fill = text_color, font = font)
        d.text((640, 441), self.response["currency"], fill = text_color, font = font)
        d.text((640, 507), self.response["currency"], fill = text_color, font = font)
        d.text((640, 575), self.response["currency"], fill = text_color, font = font)

        im.save("reciept_"+self.response["reciept_number"]+".pdf")