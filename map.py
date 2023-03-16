import csv
import ast
import pygame
from Block import Block



def new_map(sc, path_file, block_list, color_list):
    path = f'./data/map/{path_file}.csv'
    fied_names = ['x', 'y', 'width', 'height', 'color']
    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=fied_names)
        writer.writeheader()
        for block in block_list:
            bk_color = Block(block,sc).rand_color(color_list)
            block_data = {
                    'x': block.x,
                    'y': block.y,
                    'width': block.width,
                    'height': block.height,
                    'color': bk_color
                }
            
            writer.writerow(block_data)

    

def open_map(sc, path_file):
    try:
        path = f'./data/map/{path_file}'
        file = open(path, newline='')
        reader = csv.reader(file)
    except FileExistsError:
        print(f"[ERRO] Arquivo '{path_file}' nao encontrado em data/map")

    header = next(reader)
    data = []

    for row in reader:
        x = int(row[0])
        y = int(row[1])
        width = int(row[2])
        height = int(row[3])
        color = ast.literal_eval(row[4])
        data.append([x, y, width, height, color])

        block = pygame.Rect(x, y, width, height)
        Block(block, sc).select_color(color)


def save_map(sc, block_list, path_file):
    path = f'./data/map/{path_file}'
    fied_names = ['x', 'y', 'width', 'height', 'color']
    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=fied_names)
        writer.writeheader()
        for block in block_list:
            color = sc.get_at((block.x, block.y))
            block_data = {
                    'x': block.x,
                    'y': block.y,
                    'width': block.width,
                    'height': block.height,
                    'color': color
                }
            
            writer.writerow(block_data)
        print('SAVED')

    
def filter(sc, block_list):
    block_selected = []
    for block in block_list:
        color = sc.get_at((block.x, block.y))
        block_data = {
                'x': block.x,
                'y': block.y,
                'width': block.width,
                'height': block.height,
                'color': color
            }
        block_selected.append(block_data)
    
    return block_selected