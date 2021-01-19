from random import randint
import pygame


class KeyDispatcher():
    def __init__(self):
        self.pressed_key_func_dict = []

    def dispatch(self, event, state):
        if (event.type == pygame.KEYDOWN):
            for el in self.pressed_key_func_dict[state]:
                el(event)


class Door():

    def __init__(self, x, y):
        self.pic = pygame.image.load("pics\door\door1.png")
        self.pos = (x, y)
        self.op_cl_flag = False
        self.rect = pygame.Rect(self.pos, (50, 50))

    def draw_door(self, gameDisplay, count):
        if self.op_cl_flag == False:
            gameDisplay.blit(self.pic, self.pos)


class Text():

    def draw_text_gold(self, gameDisplay, hero, f1):
        pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 800, 800, 750))

        text1 = f1.render(hero.text, True, (180, 0, 0))
        gameDisplay.blit(text1, (50, 850))

        text2 = f1.render(str(hero.money), True, (180, 0, 0))
        gameDisplay.blit(text2, (600, 850))


class Shop():

    def __init__(self, x, y):
        self.pic = pygame.image.load("pics\shop\shop3.png")
        self.pos = (x, y)
        self.dialog_count = 0
        self.rect = pygame.Rect(self.pos, (50, 50))

    def draw_shop(self, gameDisplay, count):
        gameDisplay.blit(self.pic, self.pos)


class Barrier():

    def __init__(self, x, y):
        self.pic = [pygame.image.load("pics\light\l1.png"),
                    pygame.image.load("pics\light\l2.png"),
                    pygame.image.load("pics\light\l3.png"),
                    pygame.image.load("pics\light\l4.png"),
                    pygame.image.load("pics\light\l5.png"),
                    pygame.image.load("pics\light\l6.png")]
        self.pos = (x, y)
        self.rect = pygame.Rect(self.pos, (50, 50))
        self.op_cl_flag = False

    def draw_barrier(self, gameDisplay, count):
        if self.op_cl_flag == False:
            gameDisplay.blit(self.pic[int((count / 2) % 6)], self.pos)


class GameObject():

    def __init__(self, x, y, pics_list):
        self.pos = (x, y)
        self.pic = pics_list
        self.rect = pygame.Rect(self.pos, (50, 50))


class Coin(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y,
                         [pygame.image.load("pics\coin\coin1.png"),
                          pygame.image.load("pics\coin\coin2.png"),
                          pygame.image.load("pics\coin\coin3.png"),
                          pygame.image.load("pics\coin\coin4.png"),
                          pygame.image.load("pics\coin\coin5.png"),
                          pygame.image.load("pics\coin\coin6.png")])

    def draw_coin(self, gameDisplay, count, coins):
        for el in coins:
            gameDisplay.blit(el.pic[int(count / 2 % 6)], el)


class Chest(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("pics\chest\chest.png"))

    def draw_chest(self, gameDisplay, count, chests):
        for el in chests:
            gameDisplay.blit(el.pic, el)


class Key(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.transform.scale(pygame.image.load("pics\key\key.png"), (50, 50)))

    def draw_key(self, gameDisplay, count, hero_key):
        if hero_key == True:
            gameDisplay.blit(self.pic, self.pos)


class Star():

    def __init__(self, x, y):
        self.pic = [pygame.image.load("pics\chest\star1.png"),
                    pygame.image.load("pics\chest\star2.png")]
        self.pos = (x, y)

    def draw_stars(self, gameDisplay, count, stars):
        for el in stars:
            gameDisplay.blit(self.pic[int(count / 4 % 2)], (el.pos[0], el.pos[1] - 5))


class Hero():

    def __init__(self, x, y):
        self.pic = [pygame.image.load("man\man3.png"),
                    pygame.image.load("man\man4.png"),
                    pygame.image.load("man\man5.png"),
                    pygame.image.load("man\man6.png"),
                    pygame.image.load("man\man7.png"),
                    pygame.image.load("man\man8.png"),
                    pygame.image.load("man\man9.png"),
                    pygame.image.load("man\man10.png"),
                    pygame.image.load("man\man11.png"),
                    pygame.image.load("man\man12.png")]
        # self.her_x = x
        # self.her_y = y
        # self.pos = (self.her_x, self.her_y)
        self.money = 0
        self.key = False
        self.text = ""
        self.wallkc = 0
        self.wallkpos = (0, 0)
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw_hero(self, gameDisplay, count):
        gameDisplay.blit(self.pic[int(count / 2 % 10)], (self.rect))


class Lever():

    def __init__(self, x, y):
        self.pic = [pygame.image.load("pics\lever\lev1.png"),
                    pygame.image.load("pics\lever\lev2.png")]
        self.pos = (x, y)
        self.swich = False
        self.rect = pygame.Rect(self.pos, (50, 50))

    def draw_lever(self, gameDisplay, count):
        if self.swich == False:
            gameDisplay.blit(self.pic[0], self.pos)
        else:
            gameDisplay.blit(self.pic[1], self.pos)


class Exit():

    def __init__(self, x, y):
        self.pic = [pygame.image.load("pics\exit\exit1.png"),
                    pygame.image.load("pics\exit\exit2.png")]
        self.pos = (x, y)
        self.rect = pygame.Rect(self.pos, (50, 50))

    def draw_exit(self, gameDisplay, count):
        gameDisplay.blit(self.pic[int(count / 4 % 2)], self.pos)


class Wall(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("wall.jpg"))

    def draw_wall(self, gameDisplay, walls):
        for el in walls:
            gameDisplay.blit(self.pic, el)

    @staticmethod
    def wall_list_def(wall_binary):
        x = 0
        y = 0
        wall_list = []

        for el in wall_binary:
            wall_list.append((x, y)) if el == 1 else 0
            x += 50
            if x > 750:
                x = 0
                y += 50

        return [Wall(*x) for x in wall_list]

    def is_collide(self, test_rect):
        return test_rect.colliderect(self.rect)



class StateMachine():
    def __init__(self, dict_of_states):
        self.dict_of_states = dict_of_states
        self.state = "menu"
        self.gameEnd = False

    def run(self, gameDisplay):
        if self.dict_of_states[self.state].execute(gameDisplay):
            self.change_state()

    def change_state(self):

        if self.state == "menu":
            self.state = "level_1"
        elif self.state == "level_1":
            self.state = "over"
        elif self.state == "over":
            self.gameEnd = True
        # else:
        #     self.state = 0

        # self.state = 0 if self.state > 1 else self.state + 1


class GameMenu():
    def __init__(self, pic):
        self.pic = pic
        self.is_gamover = False

    def execute(self, gameDisplay):
        gameDisplay.blit(self.pic, (0, 0))
        return self.is_gamover

    def press_key(self, event):
        if event.key == pygame.K_RETURN:
            self.is_gamover = True


class GameOver():
    def __init__(self, pic):
        self.pic = pic
        self.is_gamover = False

    def execute(self, gameDisplay):
        gameDisplay.blit(self.pic, (0, 0))
        return self.is_gamover

    def press_key(self, event):
        if event.key == pygame.K_RETURN:
            self.is_gamover = True


class DungeonKeeper():
    def __init__(self, background, f1):
        self.f1 = f1
        self.hero = Hero(50, 700)
        self.lever = Lever(700, 50)
        self.exit = Exit(700, 700)
        self.key = Key(700, 825)
        # chests = [Chest(350, 600), Chest(250, 50), Chest(350, 50)]
        self.chests = [Chest(350, 600)]
        self.stars = [Star(350, 600)]
        # coins = [Coin(50, 50), Coin(200, 250), Coin(450, 50), Coin(300, 300), Coin(450, 700), Coin(500, 500)]
        self.coins = [Coin(500, 500)]
        self.door = Door(600, 250)
        self.shop = Shop(700, 350)
        self.barrier = Barrier(600, 650)
        self.background = background
        self.count = 0
        self.text = Text()
        self.is_gamover = False
        wall_sceme =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1,
                       1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1,
                       1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1,
                       1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1,
                       1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1,
                       1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1,
                       1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1,
                       1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
                       1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1,
                       1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1,
                       1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1,
                       1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1,
                       1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1,
                       1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.walls = Wall.wall_list_def(wall_sceme)

        # self.coin = Coin()

        self.test_rect = None

    def action_move(self, event):
        # print(event)
        if event.key == pygame.K_LEFT:
            wanted_move = (-50, 0)
        elif event.key == pygame.K_RIGHT:
            wanted_move = (50, 0)
        elif event.key == pygame.K_UP:
            wanted_move = (0, -50)
        elif event.key == pygame.K_DOWN:
            wanted_move = (0, 50)
        else:
            wanted_move = (0, 0)

        self.test_rect = pygame.Rect(self.hero.rect[0] + wanted_move[0],
                                     self.hero.rect[1] + wanted_move[1],
                                     50, 50)
        self.move_chek()

    def move_chek(self):
        if self.test_rect.colliderect(self.door.rect) and self.hero.key == False:
            self.hero.text = "Дверь закрыта..."

        elif self.test_rect.colliderect(self.door.rect) and self.hero.key == True and \
                self.door.op_cl_flag == False:
            self.door.op_cl_flag = True

        elif self.test_rect.colliderect(self.barrier.rect) and self.barrier.op_cl_flag == False:
            self.hero.text = "смерти жаждешь?????"

        # for el in self.walls:
        #     if el.is_collide(self.test_rect):
        #
        elif not any([(x.is_collide(self.test_rect)) for x in self.walls]):
            self.hero.rect = self.test_rect
        #
        # elif (self.test_rect[0], self.test_rect[1]) not in self.wall_list:
        #     self.hero.rect = self.test_rect

    # def take_exit(self):
    #     if self.hero.rect.colliderect(self.exit.rect):
    #         self.is_gamover = True

    def take_coin(self):
        for el in self.coins:
            if self.hero.rect.colliderect(el.rect):
                self.hero.money += 100
                self.coins.pop(self.coins.index(el))

    def take_chest(self):
        for el in self.chests:
            if self.hero.rect.colliderect(el.rect):
                self.hero.money += randint(200, 500)
                self.chests.pop(self.chests.index(el))

    def lever_interaction(self, event):
        if self.hero.rect.colliderect(self.lever.rect) and event.key == pygame.K_RETURN:
            self.lever.swich = True
            self.barrier.op_cl_flag = True

    def shop_interaction(self, event):

        if self.hero.rect.colliderect(self.shop.rect) and self.shop.dialog_count == 0 and event.key == pygame.K_RETURN:
            self.hero.text = "Ключ в обмен на все! золото лабиринта"
            self.shop.dialog_count += 1

        elif self.hero.rect.colliderect(self.shop.rect) and self.shop.dialog_count == 1 and self.chests == [] \
                and self.coins == [] and self.hero.key == False and event.key == pygame.K_RETURN:
            self.hero.text = "Отдай золото - бери ключ"
            self.hero.key = True
            self.hero.money = 0

        elif self.hero.rect.colliderect(
                self.shop.rect) and self.shop.dialog_count == 1 and self.hero.key == False \
                and event.key == pygame.K_RETURN:
            self.hero.text = "Я сказал ВСЕ ДЕНЬГИ!!!!"

        elif self.hero.rect.colliderect(self.shop.rect) and self.hero.key == True and event.key == pygame.K_RETURN:
            self.hero.text = "У меня ничего нет... не мешай спать."

    def exit_interaction(self, event):
        if self.hero.rect.colliderect(self.exit.rect) and event.key == pygame.K_RETURN:
            self.is_gamover = True

    def execute(self, gameDisplay):

        gameDisplay.blit(self.background, (0, 0))
        self.shop.draw_shop(gameDisplay, self.count)
        self.walls[0].draw_wall(gameDisplay, self.walls)
        self.lever.draw_lever(gameDisplay, self.count)
        self.exit.draw_exit(gameDisplay, self.count)
        self.door.draw_door(gameDisplay, self.count)
        self.text.draw_text_gold(gameDisplay, self.hero, self.f1)
        self.key.draw_key(gameDisplay, self.count, self.hero.key)
        if self.coins:
            self.coins[0].draw_coin(gameDisplay, self.count, self.coins)
        if self.chests:
            self.chests[0].draw_chest(gameDisplay, self.count, self.chests)
            self.stars[0].draw_stars(gameDisplay, self.count, self.chests)
        self.barrier.draw_barrier(gameDisplay, self.count)
        self.hero.draw_hero(gameDisplay, self.count)

        self.take_chest()
        self.take_coin()

        self.count = self.count + 1 if self.count <= 106 else 0

        # self.take_exit()

        return self.is_gamover
