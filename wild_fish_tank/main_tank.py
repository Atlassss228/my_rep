import pygame
from fishy_draw import *
from random import randint
from math import sin, cos, sqrt

pygame.init()

deikstra_dict = {}

gameDisplay = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("no_way_out!!!")

backgroung = pygame.image.load("pics/background/rear.jpg")

obstacle_pos = ((500, 350),)

green_fish = {"move": [pygame.transform.scale(pygame.image.load("pics/greenfifh/gfr_move1.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/greenfifh/gfr_move2.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/greenfifh/gfl_move1.png"), (50, 50)),
                       pygame.transform.scale(pygame.image.load("pics/greenfifh/gfl_move2.png"), (50, 50))],
              "pos": [0, 500], "dir": "r", "rect": pygame.Rect(0, 500, 50, 50)}

green_fish["center"] = [green_fish["pos"][0] + 25, green_fish["pos"][1] + 25]

first_obstacle = {"pos": obstacle_pos[0], "rect": pygame.Rect(obstacle_pos[0], (300, 300)),
                  "g_points": []}


def dist(p1coor, p2coor):
    dist = sqrt(((p1coor[0] - p2coor[0]) ** 2 + (p1coor[1] - p2coor[1]) ** 2))
    return  round (dist, 3)


def g_points_creator(rect):
    gp_dict = {}
    gp_dict["b"] = ((rect[0] - 30, rect[1] - 30))
    gp_dict["e"] = ((rect[0] + 330, rect[1] - 30))
    gp_dict["d"] = ((rect[0] - 30, rect[1] + 330))
    gp_dict["c"] = ((rect[0] + 330, rect[1] + 330))
    gp_dict["a"] = (green_fish["center"])
    gp_dict["f"] = ((1000 + 25, 500 + 25))
    # print(gp_list)
    return gp_dict


# g_points_creator(first_obstacle["rect"])

clock = pygame.time.Clock()

f1 = pygame.font.Font(None, 36)

count = 0

ellips_x = 0
ellips_y = 0
# t = 0

gameExit = False
while not gameExit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True
            # quit()

    a = 600
    b = 400
    gameDisplay.blit(backgroung, (0, 0))

    green_fish_draw(green_fish, ellips_x, count, gameDisplay)

    pygame.draw.rect(gameDisplay, (255, 255, 255), rect=(1000, 500, 50, 50), width=5)

    pygame.draw.rect(gameDisplay, (255, 255, 255), first_obstacle["rect"], width=5)

    gp_dict = g_points_creator(first_obstacle["rect"])

    line_count = 0
    line_list = []
    for el in gp_dict:
        for i in gp_dict:

            clipped_line = first_obstacle["rect"].clipline(gp_dict[el], gp_dict[i])
            if clipped_line:
                start, end = clipped_line
                x1, y1 = start
                x2, y2 = end
            else:
                if i != el and (i,el) not in line_list:
                    line_list.append((el, i))

        print(line_list)
    # sec_conter = 65
    for node in gp_dict:
        dict_add = {}
        for line in line_list:

            if node in line:
                x = line[1] if line[0] == node else line[0]

                dict_add[x] = (dist(gp_dict[line[0]], gp_dict[line[1]]))
                deikstra_dict[node] = dict_add

    print(deikstra_dict)

    for el in line_list:

        pygame.draw.line(gameDisplay, (255, 255, 255), gp_dict[el[0]], gp_dict[el[1]], width=1)



    for el in gp_dict:

        pygame.draw.circle(gameDisplay, (255, 255, 255), gp_dict[el], 3, width=0)

    pygame.draw.rect(gameDisplay, (255, 255, 255), green_fish["rect"], width=1)

    # if t == 360:
    #     t = 0
    #
    # t += 0.005
    #
    # ellips_x = 800 + a * cos(t)
    # ellips_y = 450 + b * sin(t)
    #
    # pygame.draw.ellipse(gameDisplay, (255, 255, 255), rect=(ellips_x,ellips_y, 70, 50), width=10)
    #
    # ellips_x += 1

    # AB =  sqrt(((ellips_x - green_fish["pos"][0])**2 + (ellips_y - (green_fish["pos"][1]))**2))
    #
    # green_fish["pos"][0] += (ellips_x - green_fish["pos"][0])/AB * 2
    # green_fish["pos"][1] += (ellips_y - green_fish["pos"][1])/AB * 2

    pygame.display.update()
    clock.tick(200)

    count = 0 if count == 999 else count + 1

pygame.quit()
