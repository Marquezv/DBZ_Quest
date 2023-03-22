import pygame
import pygame.gfxdraw

class Player():
    def __init__(self, sc):
        self.sc = sc
        self.color = [255, 0, 0]
        self.x = 399 
        self.y = 399 
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        self.draw = pygame.draw.rect(self.sc, self.color, self.rect) 
        pygame.display.update()


    def handle_keys(self, key, ht):
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        if key[pygame.K_a]:
            self.x -= 21
        if key[pygame.K_d]:
            self.x += 21
        if key[pygame.K_w]:
            self.y -= 21
        if key[pygame.K_s]:
            self.y += 21
        
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        history(self.sc, self.rect, ht)

        pygame.draw.rect(self.sc, self.color, self.rect)
        radar(self)
        if key[pygame.K_LCTRL] and key[pygame.K_s]:
            clean(self.sc, ht[1])
        return self.rect
        

def history(sc, block, ht):
    x = block.x 
    y = block.y 
    block_data = to_block(sc, x, y, block.width, block.height)

    if block_data.get('color') != (255, 0, 0, 255):
        ht.append(block_data)
       
    if len(ht) > 2 :
        ht.pop(0)
    ht_color = ht[0].get('color')
    rect = pygame.Rect(ht[0].get('x'), ht[0].get('y'), ht[0].get('height'), ht[0].get('width'))
    pygame.draw.rect(sc, ht_color, rect)



def clean(sc, block):
    ht_color = block.get('color')
    rect = pygame.Rect(block.get('x'), block.get('y'), block.get('height'), block.get('width'))
    pygame.draw.rect(sc, ht_color, rect)

def to_block(sc, x, y, width, height):
    color = sc.get_at((x, y))
    block_data = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'color': color
        }
    return block_data

def radar(self):
    x = self.x - 63
    y = self.y - 63
    pygame.gfxdraw.box(self.sc, pygame.Rect(x, y,147,147), (0,0,0,100))