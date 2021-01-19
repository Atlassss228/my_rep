from random import randint
import pygame

green_fish = {"move": [pygame.transform.scale(pygame.image.load("pics/greenfifh/gfr_move1.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/greenfifh/gfr_move2.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/greenfifh/gfl_move1.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/greenfifh/gfl_move2.png"), (50, 50))],
              "pos": [600, 600],
              "prev_pos": [500, 500],
              "dir": "r",
              "rect": pygame.Rect(0, 500, 50, 50)
              }


def green_constructor(num_of_obj, obj_list, obstacle_dict):
    for el in range(num_of_obj):
        while True:
            x = [50 * (randint(50, 1500) // 50), 50 * (randint(50, 800) // 50)]
            if tuple(x) not in obstacle_dict:
                green_fish["prev_pos"] = x.copy()
                obstacle_dict[tuple(x)] = tuple(x)
                green_fish["pos"] = x.copy()
                obj_list.append(green_fish.copy())
                break

small_fish = {"move": [pygame.transform.scale(pygame.image.load("pics/smallfish/s_fish1.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/smallfish/s_fish2.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/smallfish/s_fish3.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/smallfish/s_fish4.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/smallfish/s_fish5.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/smallfish/s_fish6.png"), (50, 50))],
              "pos": [500, 500],
              "prev_pos": [0, 0],
              "dir": "r",
              "rect": pygame.Rect(500, 500, 50, 50)}


def small_constructor(num_of_obj, obj_list, obstacle_dict):
    for el in range(num_of_obj):
        while True:
            x = [50 * (randint(50, 1500) // 50), 50 * (randint(50, 800) // 50)]
            if tuple(x) not in obstacle_dict:
                small_fish["prev_pos"] = x.copy()
                obstacle_dict[tuple(x)] = tuple(x)
                small_fish["pos"] = x.copy()
                obj_list.append(small_fish.copy())
                break



jelly_fish = {"move": [pygame.transform.scale(pygame.image.load("pics/medusa/m1.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/medusa/m2.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/medusa/m3.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/medusa/m4.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/medusa/m5.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/medusa/m6.png"), (50, 50))],
              "pos": [600, 600],
              "prev_pos": [500, 500],
              "dir": "r",
              "rect": pygame.Rect(0, 500, 50, 50)
              }


def jelly_constructor(num_of_obj, obj_list, obstacle_dict):
    for el in range(num_of_obj):
        while True:
            x = [50 * (randint(50, 1500) // 50), 50 * (randint(50, 800) // 50)]
            if tuple(x) not in obstacle_dict:
                jelly_fish["prev_pos"] = x.copy()
                obstacle_dict[tuple(x)] = tuple(x)
                jelly_fish["pos"] = x.copy()
                obj_list.append(jelly_fish.copy())
                break


sea_weed = {"move": [pygame.transform.scale(pygame.image.load("pics/seaweed/1.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/2.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/3.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/4.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/5.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/6.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/7.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/8.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/9.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/10.png"), (50, 50)),
                     pygame.transform.scale(pygame.image.load("pics/seaweed/11.png"), (50, 50))],
            "pos": [600, 600],
            "prev_pos": [500, 500],
            "growth": 0,
            "dir": "r",
            "rect": pygame.Rect(0, 500, 50, 50)
            }


def weed_constructor(num_of_obj, obj_dict, obstacle_dict):
    for el in range(num_of_obj):
        while True:
            x = [50 * (randint(50, 1500) // 50), 50 * (randint(50, 800) // 50)]

            if tuple(x) not in obstacle_dict:
                sea_weed["prev_pos"] = x.copy()
                obstacle_dict[tuple(x)] = tuple(x)
                sea_weed["pos"] = x.copy()
                obj_dict[randint(0,10000)] = sea_weed.copy()
                break


stone = {"move": [pygame.transform.scale(pygame.image.load("pics/stone/stone.png"), (50, 50))],
         "pos": [250, 400], "dir": "r", "rect": pygame.Rect(500, 500, 50, 50)}

stone_pos = {(100, 600): (100, 600), (600, 100): (600, 100),
             (200, 200): (200, 200), (700, 700): (700, 700),
             (500, 350): (500, 350)}

wall = {"image": pygame.image.load("pics/wall/wall.jpg"), "lay_out": []}