import pygame

def pressed_mouse_left(sc, block_list, select_color):
    pos = pygame.mouse.get_pos()
    clicked_sprites = [bk for bk in block_list if bk.collidepoint(pos)]
    for i in clicked_sprites:
        pygame.draw.rect(sc, select_color, i)
        print(i)
        
    
