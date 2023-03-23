import pygame
from map import open_map

COLOR_PLAYER = (255, 0, 0, 255)

class Player():
    def __init__(self, sc, dragon_sphere_color):
        self.sc = sc
        self.color = COLOR_PLAYER
        self.sphere = dragon_sphere_color
        self.x = 399 
        self.y = 399 
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        self.point = 0

    def start(self, ht, ht_rd):
        block = pygame.Rect(self.x, self.y, self.height, self.width)
        history(self.sc, block, self.color, ht)
        pygame.draw.rect(self.sc, self.color, self.rect)
        radar(self, ht_rd)
        print('started')

    def handle_keys(self, key, ht, ht_rd):
        history_rd(self, ht_rd)
            
        if key[pygame.K_a]:
            self.x -= 21
            self.y += 0
            draw_player(self, ht_rd, ht)
        if key[pygame.K_d]:
            self.x += 21
            self.y += 0
            draw_player(self, ht_rd, ht)
        if key[pygame.K_w] and not key[pygame.K_a] and not key[pygame.K_d]:
            self.y -= 21
            self.x  += 0
            draw_player(self, ht_rd, ht)
        if key[pygame.K_s] and not key[pygame.K_a] and not key[pygame.K_d]:
            self.y += 21
            self.x  += 0
            draw_player(self, ht_rd, ht)
        if key[pygame.K_LCTRL] and key[pygame.K_s]:
            clean(self.sc, ht[1])
            history_rd(self, ht_rd)
            
        
def draw_player(self, ht_rd, ht):
    radar(self, ht_rd)
    self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
    history(self.sc, self.rect, self.color, ht)
    pygame.draw.rect(self.sc, self.color, self.rect)
   
# def collect_sphere(self):


def history(sc, block,color, ht):
    x = block.x 
    y = block.y 
    block_data = to_block(sc, x, y, block.width, block.height)

    if block_data.get('color') != color:
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


def radar(self, ht_rd):
    color_player = COLOR_PLAYER
    for i in range(7):
        for j in range(7):    
            xi = self.x - 63 + (21 * i)
            yi = self.y - 63 + (21 * j)
            x = self.x - 63
            y = self.y - 63
            xmax = self.x - 63 + (21 * 6)
            ymax = self.y - 63 + (21 * 6)
            block = to_block(self.sc, xi, yi, 20, 20)
            
            if block.get('color') != color_player and block_center(self, xi, yi) != self.sphere:
                ht_rd.append(block)
                draw_radar(self, color_player, x, y, xi, yi, xmax, ymax)
                

def draw_radar(self, color_player, x, y, xi, yi, xmax, ymax):
    if xi == x :
        rect = pygame.Rect(xi, yi, 3, 20)
        pygame.draw.rect(self.sc, color_player, rect)
    if xi == xmax :
        rect = pygame.Rect(xmax + 17, yi, 3, 20)
        pygame.draw.rect(self.sc, color_player, rect)
    if yi == y :
        rect = pygame.Rect(xi, yi, 20, 3)
        pygame.draw.rect(self.sc, color_player, rect)
    if yi == ymax :
        rect = pygame.Rect(xi, ymax + 17, 20, 3)
        pygame.draw.rect(self.sc, color_player, rect)

def history_rd(self, ht_rd):
    for block in ht_rd:

        if block.get('color') != COLOR_PLAYER or block_center(self, block) != self.sphere:
            rect = pygame.Rect(block.get('x'), block.get('y'), block.get('height'), block.get('width'))
            pygame.draw.rect(self.sc, block.get('color'), rect)


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

def block_center(self, x, y):
    x += 10
    y += 10
    return self.sc.get_at((x, y))