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
        history(self.rect, ht, self.sc, self.color)
        pygame.draw.rect(self.sc, self.color, self.rect)
#         radar(self.rect, self.sc)


# def radar(player, sc):
#     pygame.draw.rect(sc, [255, 0, 0], [399, 399, 42, 42], 1)
    
def history(block, ht, sc, player_color):

    color = sc.get_at((block.x, block.y))
    block_data = {
            'x': block.x,
            'y': block.y,
            'width': block.width,
            'height': block.height,
            'color': color
        }
    if block_data.get('color') != player_color:
        ht.append(block_data)
       
    if len(ht) > 2 :
        ht.pop(0)
    ht_color = ht[0].get('color')
    rect = pygame.Rect(ht[0].get('x'), ht[0].get('y'), ht[0].get('height'), ht[0].get('width'))
    pygame.draw.rect(sc, ht_color, rect)