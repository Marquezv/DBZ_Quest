from pygame import draw
from random import randint

class Block():
    color = ""
    def __init__(self, block, sc):
        self.sc = sc
        self.block_obj = block
        self.color = [0, 0, 0]

    def select_color(self, color):
        self.color = color
        self.rect = draw.rect(self.sc, self.color, self.block_obj)



    def rand_color(self, colors):
        self.color = colors[randint(0, 2)].cor
        self.rect = draw.rect(self.sc, self.color, self.block_obj)
        return self.color


