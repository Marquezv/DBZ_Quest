from Block import Block

def new_map(sc, block_list, color_list):
    f = open("data/map/01.txt", "w")
    for block in block_list:
            bk = Block(block, color_list, sc)
            f.write(f"\nx={block.x}, y={block.y}, width={block.width}, height={block.height}, color={bk.num_color}")
