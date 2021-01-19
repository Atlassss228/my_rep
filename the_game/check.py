import pygame


pygame.init()
gameDisplay = pygame.display.set_mode((800, 900))
pygame.display.set_caption("no_way_out!!!")
start = pygame.image.load("pics\start\start_screen.png")
background = pygame.image.load("rear.jpg")
end = pygame.image.load("pics\gameover\gamover.png")
clock = pygame.time.Clock()


class StateMachine():
    def __init__(self, dict_of_states):
        self.list_of_states = dict_of_states
        self.state = "menu"
        self.applicaton_end = None

    def run(self, gameDisplay):
        if self.list_of_states[self.state].execute(gameDisplay):
            self.change_state()

            # print(self.state)

    def change_state(self):

        if self.state == "menu":
            self.state = "over"
        elif self.state == "over":
            self.applicaton_end = True
            # self.state = "menu"

        # self.state = 0 if self.state > 2 else self.state + 1


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

class KeyDispatcher():
    def __init__(self):
        self.pressed_key_func_dict = {}

    def dispatch(self, event, state):
        if (event.type == pygame.KEYDOWN):
            for el in self.pressed_key_func_dict[state]:
                el(event)

key_d = KeyDispatcher()

menu = GameMenu(start)
over = GameOver(end)

key_d.pressed_key_func_dict["menu"] = menu.press_key
key_d.pressed_key_func_dict["over"] = over.press_key

sm = StateMachine({"menu": menu, "over": over})


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        # print(event)
        key_d.dispatch(event, sm.state)
    sm.run(gameDisplay)
    # gameExit = not over.is_gamover

    gameExit = sm.applicaton_end
    pygame.display.update()
    clock.tick(24)

pygame.quit()



















