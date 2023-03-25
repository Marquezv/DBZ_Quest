import random
from Player import Player, block_center

class Ia():
    def __init__(self, sc, player: Player, color_list):
        self.sc = sc
        self.width = 147
        self.height = 147
        self.player = player
        self.color_list = color_list
        self.ht_ia = []

    def update(self, player):
        scan_area(self)
        
def scan_area(self):
    scan_area = []

    color_player = self.player.color
    for i in range(7):
        for j in range(7):
            x = self.player.x - 63
            y = self.player.y - 63 
            xi = self.player.x - 63 + (21 * i)
            yi = self.player.y - 63 + (21 * j)

            
            block = to_block(xi, yi, 20, 20, block_center(self.player, xi, yi))

            scan_area.append(block)
            if len(scan_area) > 49 :
                scan_area = scan_area[:49]
                scan_area.append(block)

    scan_matrix(process_scan(self, scan_area))

def process_scan(self, scan_area):
    values_area = []
    
    for block in scan_area:
        value = 0
        
        if list(block.get('color')) == self.color_list[0].cor:
            value = self.color_list[0].valor
        if list(block.get('color')) == self.color_list[1].cor:
            value = self.color_list[1].valor
        if list(block.get('color')) == self.color_list[2].cor:
            value = self.color_list[2].valor
        if list(block.get('color')) == self.player.color:
            value = 0
        if block.get('color') == self.color_list[3].cor:
            value = self.color_list[3].valor
        
        values_area.append(value)
    area = list(min_slice(values_area, 7))
    return area

def scan_matrix(area):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    for i in area:
        l1.append(i[0])
        l2.append(i[1])
        l3.append(i[2])
        l4.append(i[3])
        l5.append(i[4])
        l6.append(i[5])
        l7.append(i[6])
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