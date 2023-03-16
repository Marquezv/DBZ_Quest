import pygame


class Player():
    pass_color = []
    def __init__(self, sc):
        self.sc = sc
        self.color = [255, 0, 0]
        self.x = 399 
        self.y = 399 
        self.width = 20
        self.height = 20
    
    def handle_keys(self, key, ht):
        
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
        radar(self.sc, self.rect)
        if key[pygame.K_LCTRL] and key[pygame.K_s]:
            clean(self.sc, ht[1])
          
           

def clean(sc, block):
    ht_color = block.get('color')
    rect = pygame.Rect(block.get('x'), block.get('y'), block.get('height'), block.get('width'))
    print(rect)
    pygame.draw.rect(sc, ht_color, rect)

def history(sc, block, ht):
    x = block.x + 10
    y = block.y + 10
    color = sc.get_at((x, y))
    block_data = {
            'x': block.x,
            'y': block.y,
            'width': block.width,
            'height': block.height,
            'color': color
        }
    if block_data.get('color') != (255, 0, 0, 255):
        ht.append(block_data)
       
    if len(ht) > 2 :
        ht.pop(0)
    ht_color = ht[0].get('color')
    rect = pygame.Rect(ht[0].get('x'), ht[0].get('y'), ht[0].get('height'), ht[0].get('width'))
    pygame.draw.rect(sc, ht_color, rect)


def radar(sc, player):
    x = player.x - 63
    y = player.y - 63
    rect = pygame.Rect(x, y, 147, 147)
    pygame.draw.rect(sc, (255, 0, 0, 255), rect, 1)

