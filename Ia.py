import random
from Player import Player, block_center, radar_out_screen

class Ia():
    def __init__(self, sc, player: Player, color_list):
        self.sc = sc
        self.width = 147
        self.height = 147
        self.player = player
        self.color_list = color_list
        self.ht_ia = []

    def update(self):
        scan_area(self)
        move_around(self)

        
def scan_area(self):
    scan_area = []

    for i in range(7):
        for j in range(7):
            
            xi = self.player.x - 63 + (21 * i)
            yi = self.player.y - 63 + (21 * j)
            try :
                block = to_block(xi, yi, 20, 20, block_center(self.player, xi, yi))

                scan_area.append(block)
                if len(scan_area) > 49 :
                    scan_area = scan_area[:49]
                    scan_area.append(block)
            except Exception:
                pass

    scan_matrix(process_scan(self, scan_area))

def process_scan(self, scan_area):
    values_area = []
    
    for block in scan_area:
        value = 800
        
        if list(block.get('color')) == self.color_list[0].cor:
            value = self.color_list[0].valor
        if list(block.get('color')) == self.color_list[1].cor:
            value = self.color_list[1].valor
        if list(block.get('color')) == self.color_list[2].cor:
            value = self.color_list[2].valor
        if block.get('color') == self.player.color:
            value = 0
        if block.get('color') == self.color_list[3].cor:
            value = self.color_list[3].valor
        values_area.append(value)
    return values_area

def scan_matrix(values_area):
    area = list(min_slice(values_area, 7))
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    try :
        for i in area:
            l1.append(i[0])
            l2.append(i[1])
            l3.append(i[2])
            l4.append(i[3])
            l5.append(i[4])
            l6.append(i[5])
            l7.append(i[6])
    except Exception:
        pass
    scan = {
        '0': l1,
        '1': l2,
        '2': l3,
        '3': l4,
        '4': l5,
        '5': l6,
        '6': l7
    }

    for i in scan:
        print(scan[i])
    print('---------')
    ...

def to_block(x, y, width, height, color):
    block_data = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'color': color
        }
    return block_data

def min_slice(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
    return lst


def move_around(self):
    x0 = self.player.x - 63
    y0 = self.player.y - 63
    xmax = x0 + 126
    ymax = y0 + 126

    space_x = self.sc.get_width()
    space_y = self.sc.get_height() - 120

    print(space_x, space_y)

    # print(f'ponta1 = ({x0, y0})')
    # print(f'ponta2 = ({x0, ymax})')
    # print(f'ponta3 = ({xmax, y0})')
    # print(f'ponta4 = ({xmax, ymax})')
   
    if abs(x0 - 0) <= abs(xmax - 861):
        print('Esquerda')
    if abs(x0 - 0) >= abs(xmax - 861):
        print('Direita')

    if abs(y0 - 0) <= abs(ymax - 861):
        print('Topo')
    
    if abs(y0 - 0) >= abs(ymax - 861):
        print('Solo')

    print(self.player.x, self.player.y)