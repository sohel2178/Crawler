import requests
from io import BytesIO
from PIL import Image

uri = 'https://bd.daraz.io/1wDdihhJbPTF0W7wyjUghE68Op4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/53/9007/1.jpg'

image_name = 'test2.jpg'

r = requests.get(uri)

# print(r.content)

i = Image.open(BytesIO(r.content))
i.save(image_name)