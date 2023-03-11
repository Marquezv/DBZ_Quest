from pygame import draw
from random import randint
import json

class Block():
    def __init__(self, block, color_list, sc):
        self.num_color = rand_color(color_list)
        self.sc = sc
        self.rect = draw.rect(self.sc, self.num_color, block)

def rand_color(colors: list):
    return colors[randint(0, 2)].cor         

        