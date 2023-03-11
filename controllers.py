import pygame

def pressed_mouse_left(sc, block_list, select_color):
    pos = pygame.mouse.get_pos()
    clicked_sprites = [bk for bk in block_list if bk.collidepoint(pos)]
    for i in clicked_sprites:
        pygame.draw.rect(sc, select_color, i)
        
    
def change_color(event, color_list):

    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_LCTRL] and keys[pygame.K_1]:
            select_color = color_list[0].cor
        if keys[pygame.K_LCTRL] and keys[pygame.K_2]:
            select_color = color_list[1].cor
        if keys[pygame.K_LCTRL] and keys[pygame.K_3]:
            select_color = color_list[2].cor
    
    return color
