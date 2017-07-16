from PIL import Image as IM
from PIL import ImageFont as IF
from PIL import ImageDraw as ID
image1 = IM.open('blank.png')
print(image1.format,image1.size,image1.mode)
ft = IF.truetype("fonts\Test1.ttf", 200)
draw = ID.Draw( image1 )
draw.text((40,100),'hello world',font=ft,fill="black")
image1.show()