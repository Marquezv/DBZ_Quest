import pygame
from map import save_map
def pressed_mouse_left(sc, block_list, select_color):
    pos = pygame.mouse.get_pos()
    clicked_sprites = [bk for bk in block_list if bk.collidepoint(pos)]
    for i in clicked_sprites:
        pygame.draw.rect(sc, select_color, i)
        print(i)
        

def change_color(keys, color_list, select_color):
    if keys[pygame.K_LCTRL] and keys[pygame.K_1]:
        select_color = color_list[0].cor
    if keys[pygame.K_LCTRL] and keys[pygame.K_2]:
        select_color = color_list[1].cor
    if keys[pygame.K_LCTRL] and keys[pygame.K_3]:
        select_color = color_list[2].cor
    if keys[pygame.K_LCTRL] and keys[pygame.K_4]:
        select_color = color_list[3].cor
    return select_color

def save(keys, sc, block_list):
    # if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
    #     save_map(sc, block_list, 'map.csv')
    ...