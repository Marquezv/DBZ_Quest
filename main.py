import pygame
from pygame.locals import QUIT
from collections import namedtuple
from map import new_map, open_map
from controllers import pressed_mouse_left, change_color, save
from Player import Player
from Ia import Ia

pygame.init()
WIDTH, HEIGHT = 880, 1000
PIXEL = 42

sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()
block_list = [pygame.Rect(21 * i, 21 * j, 20, 20) for i in range(PIXEL) for j in range(PIXEL)]

FONT = pygame.font.SysFont("exo", 40)
COLOR_FONT = (255, 255, 255)
DRAGON_SPHERE_COLOR = (228, 108, 0, 255)

Elementos = namedtuple('Elementos', ['nome', 'cor', 'valor'])
agua = Elementos('Agua', [73, 109, 250, 255], 10)
grama = Elementos('Grama', [143, 219, 70, 255], 1)
montanha = Elementos('Montanha', [168, 118, 62, 255], 60)
dragon_sphere = Elementos('Dragon Sphere', DRAGON_SPHERE_COLOR, 100)

color_list = [
    agua,
    grama,
    montanha,
    dragon_sphere
]





ascii_art = """ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⠾⠿⠿⠿⠿⠿⠿⠷⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠉⠻⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣿⠟⢁⣀⣠⣀⡀⠀⠈⠻⣷⣄⠀⠀⠀⠀
⠀⠀⠀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀
⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⠤⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀
⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀
⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆
⣼⡏⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠙⠻⣿⡿⠿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧
⣿⡇⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣷⣶⣿⣿⣥⣄⣠⣶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⣿⡇⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣭⣿⣟⣿⡟⠛⠛⣿⣯⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⢻⣇⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⢿⣷⣾⡟⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟
⠸⣿⡀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡟⠈⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇
⠀⢻⣧⠀⠀⠀⠀⠀⠀⠙⢶⣄⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀
⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀
⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⢸⣿⣿⣿⣏⠙⠛⠋⣿⠿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⢀⣼⠟⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣆⡀⠀⠀⠀⠙⢿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⣿⣿⡗⠀⠀⠀⠀⣴⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣦⣄⣰⣶⣿⣿⣧⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣿⣿⣶⣄⣴⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def main():
    print(ascii_art)
    opt = int(input("[0] Criar novo mapa \n[1] Utlizar um mapa \n :"))
    try:
        if opt == 0:
            path_file = input("Insira o nome do novo mapa :")
            new_map(sc, path_file, block_list, color_list)
        elif opt == 1:
            print("!O ARQUIVO DEVE ESTAR EM data/map")
            path_file = input("Insira o nome do arquivo :")
            open_map(sc, path_file, DRAGON_SPHERE_COLOR)
    except ValueError:
        print("[ERRO] Numero nao encontrado")
    run()

def clean():
    rect = pygame.Rect(880, 880, 880, 120)
    pygame.draw.rect(sc, (0, 0, 0, 0), rect)

def run():
    pygame.display.set_caption('DBZ_Quest')
    select_color = None
    running = True
    ht = []
    ht_rd = []
    player = Player(sc, DRAGON_SPHERE_COLOR)
    ia = Ia(sc, player, color_list)
    while running:
        ia.update()
        clock.tick(30)
        MODE = "GAME"
        for event in pygame.event.get():                                  
            left, right, middle = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            
            if event.type == QUIT:
                running = False
                pygame.quit()
            elif keys == keys[pygame.K_SPACE]:
                player.start(ht, ht_rd)
                break
            elif event.type == pygame.KEYDOWN:
                select_color = change_color(keys, color_list, select_color)
                player.handle_keys(keys, ht, ht_rd)
                if keys[pygame.K_LCTRL]:
                    MODE = "EDIT"
                save(keys, sc, block_list)
            elif left and select_color != None:
                pressed_mouse_left(sc, block_list, select_color)

        points = FONT.render(f'Points: {player.update()}', 1, COLOR_FONT)
        mode = FONT.render(f'Mode: {MODE}', 1, COLOR_FONT)
        clean()
        sc.blit(mode, (10, 885))
        sc.blit(points, (10, 925))
        
        pygame.display.update()
        
    
    
if __name__=="__main__":
    main()