import pygame
from obj2 import *

pygame.init()
gameDisplay = pygame.display.set_mode((800, 900))
pygame.display.set_caption("no_way_out!!!")
start = pygame.image.load("pics\start\start_screen.png")
background = pygame.image.load("rear.jpg")
end = pygame.image.load("pics\gameover\gamover.png")
clock = pygame.time.Clock()
f1 = pygame.font.Font(None, 36)
count = 0

menu = GameMenu(start)
level_1 = DungeonKeeper(background, f1)
over = GameOver(end)

key_d = KeyDispatcher()

key_d.pressed_key_func_dict = {
                               "menu": [menu.press_key],
                               "level_1": [level_1.action_move,
                                           level_1.lever_interaction,
                                           level_1.shop_interaction,
                                           level_1.exit_interaction],
                                "over": [over.press_key]
                              }


sm = StateMachine({"menu": menu, "over": over, "level_1": level_1 })


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        # print(event)
        key_d.dispatch(event, sm.state)
    sm.run(gameDisplay)
    gameExit = sm.gameEnd

    pygame.display.update()
    clock.tick(24)

pygame.quit()
