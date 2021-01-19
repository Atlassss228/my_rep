import pygame
from random import randint
from wall_des import wall_of_lab

# инициализация библиотеки
pygame.init()

gameDisplay = pygame.display.set_mode((800, 900))
pygame.display.set_caption("no_way_out!!!")
wall = pygame.image.load("wall.jpg")
backgroung = pygame.image.load("rear.jpg")
start = pygame.image.load("pics\start\start_screen.png")

end = pygame.image.load("pics\gameover\gamover.png")


shop = pygame.image.load("pics\shop\shop3.png")

shop_dict = {"dialog_count": 0}

shop_pos = (700, 350)


door = pygame.image.load("pics\door\door1.png")

door_dict = {"open": False}

door_pos = (600, 250)


lever1 = pygame.image.load("pics\lever\lev1.png")
lever2 = pygame.image.load("pics\lever\lev2.png")

lev_pos = (700, 50)

lev_dict = {"swich": False}


exit1 = pygame.image.load("pics\exit\exit1.png")
exit2 = pygame.image.load("pics\exit\exit2.png")

exit_pos = (700, 700)

exit = (exit1, exit2)


bar1 = pygame.image.load("pics\light\l1.png")
bar2 = pygame.image.load("pics\light\l2.png")
bar3 = pygame.image.load("pics\light\l3.png")
bar4 = pygame.image.load("pics\light\l4.png")
bar5 = pygame.image.load("pics\light\l5.png")
bar6 = pygame.image.load("pics\light\l6.png")

bar_pos = (600, 650)

barrier = (bar1, bar2, bar3, bar4, bar5, bar6)

barrier_dict = {"open": False}


coin1 = pygame.image.load("pics\coin\coin1.png")
coin2 = pygame.image.load("pics\coin\coin2.png")
coin3 = pygame.image.load("pics\coin\coin3.png")
coin4 = pygame.image.load("pics\coin\coin4.png")
coin5 = pygame.image.load("pics\coin\coin5.png")
coin6 = pygame.image.load("pics\coin\coin6.png")

coin_pos = [(50, 50), (200, 250), (450, 50), (300, 300), (450, 700), (500, 500)]

# coin_pos = [(500, 500)]

coins = [coin1, coin2, coin3, coin4, coin5, coin6]


man2 = pygame.image.load("man\man2.png")
man3 = pygame.image.load("man\man3.png")
man4 = pygame.image.load("man\man4.png")
man5 = pygame.image.load("man\man5.png")
man6 = pygame.image.load("man\man6.png")
man7 = pygame.image.load("man\man7.png")
man8 = pygame.image.load("man\man8.png")
man9 = pygame.image.load("man\man9.png")
man10 = pygame.image.load("man\man10.png")
man11 = pygame.image.load("man\man11.png")
man12 = pygame.image.load("man\man12.png")

star1 = pygame.image.load("pics\chest\star1.png")
star2 = pygame.image.load("pics\chest\star2.png")
chest = pygame.image.load("pics\chest\chest.png")

chest_pos = [(350, 600), (250, 50), (350, 50)]
# chest_pos = []

hero = {"her_x": 50, "her_y": 700, "wall_kickin": [(0, 0), 0], "money": 0, "key": False, "text": ""}

clock = pygame.time.Clock()

wall_list = wall_of_lab

stars = [star1, star2]

hero_pics = [man3, man4, man5, man6, man7, man8, man9, man10, man11, man12]

f1 = pygame.font.Font(None, 36)

count = 0
count2 = 0
count3 = 0

move_dict = {pygame.K_LEFT: (-50, 0), pygame.K_RIGHT: (50, 0),
             pygame.K_UP: (0, -50), pygame.K_DOWN: (0, 50)}

game_state_count = 0

def hero_move(hero, event, wall_list):
    move = (hero["her_x"] + move_dict[event.key][0], hero["her_y"] + move_dict[event.key][1])

    if move == door_pos and hero["key"] == False:
        hero["text"] = "Дверь закрыта..."

    elif move == door_pos and hero["key"] == True and door_dict["open"] == False:
        door_dict["open"] = True

    elif move == bar_pos and barrier_dict["open"] == False:
        hero["text"] = "смерти жаждешь?????"

    elif move not in wall_list:
        hero["her_x"] += move_dict[event.key][0]
        hero["her_y"] += move_dict[event.key][1]

    # else:
    #     hero["wall_kickin"][0] = move
    #     hero["wall_kickin"][1] += 1
    #     print(hero["wall_kickin"])


def shop_chek(hero):
    hero_pos = (hero["her_x"], hero["her_y"])

    if hero_pos == (700, 350) and shop_dict["dialog_count"] == 0:
        hero["text"] = "Ключ в обмен на все! золото лабиринта"
        shop_dict["dialog_count"] += 1

    elif hero_pos == (700, 350) and shop_dict["dialog_count"] == 1 and chest_pos == [] \
            and coin_pos == [] and hero["key"] == False:
        hero["text"] = "Отдай золото - бери ключ"
        hero["key"] = True
        hero["money"] = 0

    elif hero_pos == (700, 350) and shop_dict["dialog_count"] == 1 and chest_pos != [] and coin_pos != []:
        hero["text"] = "Я сказал ВСЕ ДЕНЬГИ!!!!"

    elif hero_pos == (700, 350) and hero["key"] == True:
        hero["text"] = "У меня ничего нет... не мешай спать."

def lever_chek(hero):
    hero_pos = (hero["her_x"], hero["her_y"])

    if hero_pos == lev_pos:
        lev_dict["swich"] = True
        barrier_dict["open"] = True


def gather(hero):
    if (hero["her_x"], hero["her_y"]) in coin_pos:
        hero["money"] += 100
        coin_pos.pop(coin_pos.index((hero["her_x"], hero["her_y"])))

    if (hero["her_x"], hero["her_y"]) in chest_pos:
        hero["money"] += randint(200, 500)
        chest_pos.pop(chest_pos.index((hero["her_x"], hero["her_y"])))

    if (hero["her_x"], hero["her_y"]) == exit_pos:
        return True


def printer(hero):

    pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 800, 800, 750))
    if hero["wall_kickin"][1] >= 5:
        hero["wall_kickin"][1] = 0
        hero["text"] = "STOP Kikin The WALL!!!!"

    # print(printer(hero))
    text1 = f1.render(hero["text"], True, (180, 0, 0))
    gameDisplay.blit(text1, (50, 850))


    text2 = f1.render(str(hero["money"]), True, (180, 0, 0))
    # pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 800, 800, 500))
    gameDisplay.blit(text2, (600, 850))



gameExit = False
while not gameExit:
    if game_state_count == 0:
        gameDisplay.blit(start, (0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                game_state_count += 1
                break
            if event.type == pygame.QUIT:
                gameExit = True

    elif game_state_count == 1:
        for event in pygame.event.get():
            # print(event)
            if (event.type == pygame.KEYDOWN) and event.key in move_dict:
                hero_move(hero, event, wall_list)

            if (event.type == pygame.KEYDOWN) and event.key == pygame.K_RETURN:
                shop_chek(hero)
                lever_chek(hero)

            gather(hero)

            if event.type == pygame.QUIT:
                gameExit = True
                # quit()

        gameDisplay.blit(backgroung, (0, 0))

        gameDisplay.blit(shop, shop_pos)

        if door_dict["open"] == False:
            gameDisplay.blit(door, door_pos)

        if lev_dict["swich"] == False:
            gameDisplay.blit(lever1, lev_pos)
        else:
            gameDisplay.blit(lever2, lev_pos)

        for el in wall_list:
            gameDisplay.blit(wall, el)

        for el in coin_pos:
            gameDisplay.blit(coins[int(count // 1)], el)
        if count > 5:
            count = 0
        else:
            count += float(0.299999)

        for el in chest_pos:
            gameDisplay.blit(chest, el)
            el = list(el)
            gameDisplay.blit(stars[int(count3 // 1)], (el[0], el[1] - 5))
        if count3 >= 1.9:
            count3 = 0
        else:
            count3 += float(0.24)

        gameDisplay.blit(exit[int(count3 // 1)], exit_pos)

        if barrier_dict["open"] == False:
            gameDisplay.blit(barrier[int(count // 1)], bar_pos)

        gameDisplay.blit(hero_pics[int(count2 // 1)], (hero["her_x"], hero["her_y"]))
        if count2 > 9:
            count2 = 0
        else:
            count2 += float(0.5)

        printer(hero)

        if gather(hero) == True:
            game_state_count += 1

    elif game_state_count == 2:
        gameDisplay.blit(end, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

    pygame.display.update()
    clock.tick(24)

pygame.quit()
