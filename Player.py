import pygame


class Player():
    def __init__(self, sc):
        self.sc = sc
        self.color = [255, 0, 0]
        self.x = 399 
        self.y = 399 
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        pygame.draw.rect(self.sc, self.color, self.rect) 
    
    def handle_keys(self, key, ht, ht_rd):
        if key[pygame.K_a]:
            self.x -= 21
        if key[pygame.K_d]:
            self.x += 21
        if key[pygame.K_w]:
            self.y -= 21
        if key[pygame.K_s]:
            self.y += 21
        radar(self)
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        history(self.sc, self.rect, ht)
        history_rd(self, ht_rd)
    
        pygame.draw.rect(self.sc, self.color, self.rect) 
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


def radar(self):
    x = self.x - 63
    y = self.y - 63
    rd = pygame.Surface((147, 147), pygame.SRCALPHA)   
    rd.fill((100,100,100, 100))
    # rd.fill((0,0,0,0))

    # rect = pygame.Rect(x, y, 147, 147)

    self.sc.blit(rd, (x, y))
    print('change color sc1')
    
    

def history_rd(self, ht_rd):
    for i in range(7):
        for j in range(7):
            yi = self.y - 63 + (21 * j)
            xi = self.x - 63 + (21 * i)
            block_data = to_block(self.sc, xi, yi, 21, 21)
            ht_rd.append(block_data)
    clean_rd(self)
    ht_rd.clear()
    return ht_rd

def clean_rd(self):
    x = self.x - 63
    y = self.y - 63
    rd = pygame.Surface((147, 147), pygame.SRCALPHA)   
    rd.set_colorkey((0,0,0,0))
    self.sc.blit(rd, (x, y))
    print('change color sc')


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
