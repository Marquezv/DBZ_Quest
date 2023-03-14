import pygame
from pygame.locals import QUIT
from collections import namedtuple
from map import new_map, open_map, save_map
from controllers import pressed_mouse_left


pygame.init()
WIDTH, HEIGHT = 880, 880
PIXEL = 42

sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()

block_list = [pygame.Rect(21 * i, 21 * j, 20, 20) for i in range(42) for j in range(42)]

Elementos = namedtuple('Elementos', ['nome', 'cor', 'valor'])
agua = Elementos('Agua', [73, 109, 250, 98], 10)
grama = Elementos('Grama', [143, 219, 70, 86], 1)
montanha = Elementos('Montanha', [168, 118, 62, 66], 60)
player = Elementos('Player', [255, 255, 255], 0)

color_list = [
    agua,
    grama,
    montanha,
    player
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
            open_map(sc, path_file)
    except ValueError:
        print("[ERRO] Numero nao encontrado")
    run()
    

class Player(object):

    def __init__(self, sc):
        self.sc = sc
        self.color = [255, 0, 0]
        self.x = 399 
        self.y = 399 
        self.width = 20
        self.height = 20
        self.radar_x = self.x - 63
        self.radar_y = self.y - 63
        self.radar_width = 147
        self.radar_height = 147
        self.radar_color = [100, 0, 0, 100]
        self.radar_border = 3
        self.image = self.color
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        self.radar_rect = pygame.Rect(self.radar_x, self.radar_y, self.radar_height, self.radar_width)
    
    def handle_keys(self, key):
        if key[pygame.K_a]:
            self.x -= 21
        if key[pygame.K_d]:
            self.x += 21
        if key[pygame.K_w]:
            self.y -= 21
        if key[pygame.K_s]:
            self.y += 21
        return pygame.Rect(self.x, self.y, self.height, self.width)
    
        

    

player = Player(sc)

def run():
    select_color = None
    running = True
    while running:
        for event in pygame.event.get():
            left, right, middle = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            player.handle_keys(keys)
            pygame.draw.rect(sc, [255, 0, 0], player)
            if event.type == QUIT:
                running = False
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
                if keys[pygame.K_LCTRL] and keys[pygame.K_4]:
                    select_color = color_list[3].cor
                if keys[pygame.K_LCTRL] and keys[pygame.K_SPACE]:
                    save_map(sc, block_list, 'map.csv')
        
        pygame.display.update()
        clock.tick(60)
    
if __name__=="__main__":
    main()