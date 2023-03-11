import csv
from Block import Block

def to_dict(block):
        return json.loads(json.dumps(block, default=lambda o: o.__dict__))

def new_map(sc, block_list, color_list):
    fied_names = ['x', 'y', 'width', 'height', 'color']
    with open('map.csv', 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=fied_names)
        writer.writeheader()
        for block in block_list:
            bk = Block(block, color_list, sc)
            block_data = {
                'x': block.x,
                'y': block.y,
                'width': block.width,
                'height': block.height,
                'color': bk.num_color
                }
            writer.writerow(block_data)

    
# def new_map(sc, block_list, color_list):
#     f = open("data/map/01.txt", "w")
#     for block in block_list:
#             bk = Block(block, color_list, sc)
#             f.write(f"\nx={block.x}, y={block.y}, width={block.width}, height={block.height}, color={bk.num_color}")

def open_map(sc, block_list, color_list):
    f = open("data/map/01.txt", "r")
    lines = f.readlines()
    for line in lines:
        # if line.find('x=') != -1:
            print(line.split('\n')[0].lstrip())