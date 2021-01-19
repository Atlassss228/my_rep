import pygame
from fishy_draw import *
from objects import *
from random import randint
from math import sin, cos, sqrt

pygame.init()

deikstra_dict = {}

gameDisplay = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("no_way_out!!!")

backgroung = pygame.image.load("pics/background/rear2.jpg")


obstacle_dict = {}
obstacle_dict.update(wall_cord_dict)
obstacle_dict.update(stone_pos)

green = []
green_constructor(5, green, obstacle_dict)

jelly = []
jelly_constructor(5, jelly, obstacle_dict)

weed_dict = {}
weed_add_dict = {}
weed_constructor(5, weed_dict, obstacle_dict)

small = []
small_constructor(5, small, obstacle_dict)

# def dumb_fish_beh(obj, count, wall_cord):
#     temp_pos = obj["pos"].copy()
#
#     if count % 200 == 0:
#         x = randint(-1, 1)
#         y = randint(-1, 1)
#         temp_pos[0] += x * 50
#         temp_pos[1] += y * 50
#
#         if tuple(temp_pos) not in wall_cord:
#             obj["prev_pos"] = obj["pos"].copy()
#             obj["pos"] = temp_pos.copy()

def all_dumb_fish_beh(obj_list, count, obstacle_dict):
    for el in obj_list:
        temp_pos = el["pos"].copy()

        if count % 200 == 0:
            x = randint(-1, 1)
            y = randint(-1, 1)
            temp_pos[0] += x * 50
            temp_pos[1] += y * 50

            if tuple(temp_pos) not in obstacle_dict:
                obstacle_dict.pop(tuple(el["pos"]))
                el["prev_pos"] = el["pos"].copy()
                el["pos"] = temp_pos.copy()
                obstacle_dict[tuple(el["pos"])] = tuple(el["pos"])

def weed_growth(weed):
    weed_dict[weed]["growth"] += 10
    if weed_dict[weed]["growth"] == 100:
        weed_dict[weed]["growth"] = 0
        weed_constructor(1, weed_add_dict, obstacle_dict)


def weed_beh(obj_dict, count, obstacle_dict):


    for el in obj_dict:
        temp_pos = obj_dict[el]["pos"].copy()

        if count % 100 == 0:

            weed_growth(el)

            x = randint(-1, 1)
            y = randint(-1, 1)
            temp_pos[0] += x * 50
            temp_pos[1] += y * 50

            if tuple(temp_pos) not in obstacle_dict:
                obstacle_dict.pop(tuple(obj_dict[el]["pos"]))
                obj_dict[el]["prev_pos"] = obj_dict[el]["pos"].copy()
                obj_dict[el]["pos"] = temp_pos.copy()
                obstacle_dict[tuple(obj_dict[el]["pos"])] = tuple(obj_dict[el]["pos"])

    weed_dict.update(weed_add_dict)
    print(len(weed_dict))
    weed_add_dict.clear()





clock = pygame.time.Clock()

f1 = pygame.font.Font(None, 36)

count = 0

gameExit = False
while not gameExit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True
            # quit()

    gameDisplay.blit(backgroung, (0, 0))

    wall_draw(wall, gameDisplay)

    all_dumb_fish_beh(small, count, obstacle_dict)
    all_small_fish_draw(small, count, gameDisplay)

    weed_beh(weed_dict, count, obstacle_dict)
    all_weed_draw(weed_dict, count, gameDisplay)

    all_dumb_fish_beh(jelly, count, obstacle_dict)
    all_small_fish_draw(jelly, count, gameDisplay)

    all_dumb_fish_beh(green, count, obstacle_dict)
    all_green_fish_draw(green, count, gameDisplay)

    stone_draw(stone, count, gameDisplay, stone_pos)

    # print(obstacle_list)

    pygame.display.update()
    clock.tick(600)

    count = 0 if count == 999 else count + 1

pygame.quit()
