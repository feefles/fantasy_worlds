#util.py

import pyglet, math

def distance(p1=(0,0),p2=(0,0)):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def center_image(image):
    image.anchor_x=image.width/2
    image.anchor_y=image.height/2
    
