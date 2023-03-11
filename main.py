import pygame
from pygame.locals import QUIT
from collections import namedtuple
from Block import Block
from map import new_map
from controllers import change_color, change_color, pressed_mouse_left

pygame.init()
WIDTH, HEIGHT = 880, 880
PIXEL = 42

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

block_list = [pygame.Rect(21 * i, 21 * j, 20, 20) for i in range(42) for j in range(42)]

Elementos = namedtuple('Elementos', ['nome', 'cor', 'valor'])
agua = Elementos('Agua', [62, 129, 237], 10)
grama = Elementos('Grama', [62, 237, 106], 1)
montanha = Elementos('Montanha', [237, 173, 62], 60)

color_list = [
    agua,
    grama,
    montanha
]
     

new_map(sc, block_list, color_list)

def main():
    select_color = None
    while True:
        for event in pygame.event.get():
            left, right, middle = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()

            if event.type == QUIT:
                pygame.quit()
            elif left and select_color != None:
                pressed_mouse_left(sc, block_list, select_color)
            
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_LCTRL] and keys[pygame.K_1]:
                    select_color = color_list[0].cor
                if keys[pygame.K_LCTRL] and keys[pygame.K_2]:
                    select_color = color_list[1].cor
                if keys[pygame.K_LCTRL] and keys[pygame.K_3]:
                    select_color = color_list[2].cor

        pygame.display.update()

        clock.tick(60)
    
main()