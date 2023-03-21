import sys, random, time
from PIL import Image, ImageDraw


SIZE = 7
LENGTH = 100

r = lambda: random.randint(0, 255)
rl = lambda: (r(), r(), r())

lc = (rl(), rl(), rl(), (0, 0, 0), (0, 0, 0), (0, 0, 0,))

color_stack = []

i = Image.new('RGB', (1500, 1500))
draw = ImageDraw.Draw(i)

for y in range(500, 1201, 100):
    hc = 0
    for x in range(400, 1001, 100):
        if hc < int(SIZE/2):    
            color = random.choice(lc)
            color_stack.append(color)
            draw.rectangle([(x, y), (x + LENGTH, y + LENGTH)], fill=color)
        if hc == int(SIZE/2):
            color = random.choice(lc)
            draw.rectangle([(x, y), (x + LENGTH, y + LENGTH)], fill=color)
        if hc > int(SIZE/2):
            color = color_stack.pop()
            draw.rectangle([(x, y), (x + LENGTH, y + LENGTH)], fill=color)
        hc += 1


i.save('inviders.jpeg', 'JPEG')
