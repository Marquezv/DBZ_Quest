import pygame
import math
from queue import PriorityQueue

from map import open_map


from Player import Player, block_center

class Ia():
    def __init__(self, sc, player: Player, color_list):
        self.sc = sc
        self.width = 147
        self.height = 147
        self.player = player
        self.color_list = color_list
        self.ht_ia = []
        self.tile = 20
        scan_map(self)
    def update(self):
        scan_area(self)
       
def scan_area(self):
    scan_area = []

    for i in range(7):
        for j in range(7):
            
            xi = self.player.x - 63 + (21 * i)
            yi = self.player.y - 63 + (21 * j)
            try :
                block = to_block(self, xi, yi, block_center(self.player, xi, yi))
                if block.get('valor') == 100:
                    find_sphere(scan_area)
                scan_area.append(block)
                if len(scan_area) > 49 :
                    scan_area = scan_area[:49]
                    scan_area.append(block)
            except Exception:
                pass
   
    return  scan_matrix(process_scan( scan_area))


def process_scan(scan_area):
    value_list = []
    for block in scan_area:
        block = block.get('valor')
        value_list.append(block)
    return value_list

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
    return area

def scan_map(self):
    sc_height = self.sc.get_height() - 120

    block_map = []
    for i in range(42):
        for j in range(42):
            xi = j * 21
            yi = i * 21
        
            color = self.sc.get_at((xi, yi))
            block = to_block(self, xi, yi, color)
            block_map.append((block.get('valor')))

    area = list(min_slice(block_map, 42))


def to_block(self, x, y, color):

    listcolor = list(color)
    value = 0
    if listcolor == self.color_list[0].cor:
        value = self.color_list[0].valor
    
    if listcolor == self.color_list[1].cor:
        value = self.color_list[1].valor

    if listcolor == self.color_list[2].cor:
        value = self.color_list[2].valor
    
    if color == self.player.color:
        value = 'x'
    
    if color == self.color_list[3].cor:
        value = self.color_list[3].valor

    block_data = {
            'x': x,
            'y': y,
            'color': color,
            'valor': value
        }
    return block_data

def min_slice(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
    return lst


def find_sphere(scan_map):
    pos_i = 0
    pos_j = 0 
    for i in range (len(scan_map)):
        for j in range(i):
            if 100 == scan_map[i].get('valor'): 
                pos_i = scan_map[i].get('x')
                pos_j = scan_map[i].get('y')
            break
    
    return (pos_i, pos_j) 

