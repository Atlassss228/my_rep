from wall_des import wall_of_lab
from obj import *
import pygame

wall_pic = pygame.image.load("wall.jpg")
backgroung = pygame.image.load("rear.jpg")

def draw_wall(gameDisplay):
    for el in wall_of_lab:
        gameDisplay.blit(wall_pic, el)

def draw_key(gameDisplay):
    if hero.key == True:
        gameDisplay.blit(key.pic, key.pos)

def draw_barrier(gameDisplay, count):
    if barrier.op_cl_flag == False:
        gameDisplay.blit(barrier.pic[int((count/2) % 6)], barrier.pos)


def draw_coin(gameDisplay, count):
    for el in coins:
        gameDisplay.blit(el.pic[int(count/2 % 6)], el)


def draw_chest_stars(gameDisplay, count):

    for el in chests:
        gameDisplay.blit(el.pic, el)
        gameDisplay.blit(star.pic[int(count/4 % 2)], (el.pos[0], el.pos[1] - 5))


def draw_shop(gameDisplay, count):
    gameDisplay.blit(shop.pic, shop.pos)


def draw_lever(gameDisplay, count):
    if lever.swich == False:
        gameDisplay.blit(lever.pic[0], lever.pos)
    else:
        gameDisplay.blit(lever.pic[1], lever.pos)


def draw_exit(gameDisplay, count):
    gameDisplay.blit(exit.pic[int(count/4 % 2)], exit.pos)


def draw_hero(gameDisplay, count):
    gameDisplay.blit(hero.pic[int(count/2 % 10)], (hero.her_x, hero.her_y))


def draw_door(gameDisplay, count):
    if door.op_cl_flag == False:
        gameDisplay.blit(door.pic, door.pos)

def draw_backgroung(gameDisplay):
        gameDisplay.blit(backgroung, (0, 0))

def draw_text_gold(gameDisplay, hero, f1):
    pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 800, 800, 750))

    text1 = f1.render(hero.text, True, (180, 0, 0))
    gameDisplay.blit(text1, (50, 850))

    text2 = f1.render(str(hero.money), True, (180, 0, 0))
    gameDisplay.blit(text2, (600, 850))