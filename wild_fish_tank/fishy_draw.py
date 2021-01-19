import pygame

def all_green_fish_draw(green_fish_list, count, gameDisplay):
    for green_fish in green_fish_list:
        if (green_fish["prev_pos"][0] - green_fish["pos"][0]) < 0:
            green_fish["dir"] = "r"
        else:
            green_fish["dir"] = "l"

        if green_fish["dir"] == "r":
            if count // 100 % 2 == 0:
                gameDisplay.blit(green_fish["move"][0], green_fish["pos"])
            else:
                gameDisplay.blit(green_fish["move"][1], green_fish["pos"])
        else:
            if count // 100 % 2 == 0:
                gameDisplay.blit(green_fish["move"][2], green_fish["pos"])
            else:
                gameDisplay.blit(green_fish["move"][3], green_fish["pos"])


def all_small_fish_draw(small_fish_list, count, gameDisplay):
     for small_fish in small_fish_list:
        if(small_fish["prev_pos"][0] - small_fish["pos"][0]) > 0:
            small_fish["dir"] = "r"
        else:
            small_fish["dir"] = "l"

        x = int(count / 30) % 6
        if small_fish["dir"] == "l":
            gameDisplay.blit(small_fish["move"][x], small_fish["pos"])

        else:
            gameDisplay.blit(pygame.transform.flip(small_fish["move"][x], True, False), small_fish["pos"])

def all_weed_draw(weed_dict, count, gameDisplay):
    for weed in weed_dict:
        if(weed_dict[weed]["prev_pos"][0] - weed_dict[weed]["pos"][0]) > 0:
            weed_dict[weed]["dir"] = "r"
        else:
            weed_dict[weed]["dir"] = "l"

        x = int(count / 20) % 11
        if weed_dict[weed]["dir"] == "l":
            gameDisplay.blit(weed_dict[weed]["move"][x], weed_dict[weed]["pos"])

        else:
            gameDisplay.blit(pygame.transform.flip(weed_dict[weed]["move"][x], True, False), weed_dict[weed]["pos"])

def stone_draw(stone, count, gameDisplay, stone_pos):
    for el in stone_pos:
        gameDisplay.blit(stone["move"][0], el)


def wall_draw(wall, gameDisplay):
    for el in wall_cord_dict:
        gameDisplay.blit(wall["image"], el)


wall_cord_dict = {}

for el in range(0, 1600, 50):
    wall_cord_dict[el, 0] = (el, 0)

for el in range(0, 1600, 50):
    wall_cord_dict[el, 850] = (el, 850)

for el in range(50, 850, 50):
    wall_cord_dict[0, el] = (0, el)

for el in range(50, 850, 50):
    wall_cord_dict[1550, el] = (1550, el)
