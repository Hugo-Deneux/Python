import pygame
import random

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

play_button = pygame.image.load('ressource/button/play.png')
play_button = pygame.transform.scale(play_button, (500,250))
play_rect = play_button.get_rect(center=(screen_width/2, screen_height/2+150))

right = pygame.image.load('ressource/button/right.png')
right = pygame.transform.scale(right, (100,100))
right_rect = right.get_rect(center=(screen_width/2+150, screen_height/2+350))

left = pygame.image.load('ressource/button/left.png')
left = pygame.transform.scale(left, (100,100))
left_rect = left.get_rect(center=(screen_width/2-150, screen_height/2+350))

enter = pygame.image.load('ressource/button/enter.png')
enter = pygame.transform.scale(enter, (100,100))
enter_rect = enter.get_rect(center=(screen_width/2+300, screen_height/2+350))

setting = pygame.image.load('ressource/button/setting.png')
setting = pygame.transform.scale(setting, (150,150))
setting_rect = setting.get_rect(center=(screen_width/2+650, screen_height/2-350))

menu_board = pygame.image.load('ressource/button/menu.png')
menu_board = pygame.transform.scale(menu_board, (531,728))
menu_rect = menu_board.get_rect(center=(screen_width/2, screen_height/2))
menu_board.set_alpha(200)

player_text = pygame.image.load('ressource/text/player.png')
player_text = pygame.transform.scale(player_text, (188,60))
player_rect = player_text.get_rect(center=(screen_width/2-125, screen_height/2-150))

circle = pygame.image.load('ressource/button/circle.png')
circle = pygame.transform.scale(circle, (200,200))
circle_rect = circle.get_rect(center=(screen_width/2-150, screen_height/2))

number1 = pygame.image.load('ressource/text/1.png')
number1 = pygame.transform.scale(number1, (133,182))
number1_rect = number1.get_rect(center=(screen_width/2-150, screen_height/2))

number2 = pygame.image.load('ressource/text/2.png')
number2 = pygame.transform.scale(number2, (133,182))
number2_rect = number2.get_rect(center=(screen_width/2, screen_height/2))

number3 = pygame.image.load('ressource/text/3.png')
number3 = pygame.transform.scale(number3, (133,182))
number3_rect = number3.get_rect(center=(screen_width/2+150, screen_height/2))

win = pygame.image.load('ressource/text/win.png')
win = pygame.transform.scale(win, (491,188))
win_rect = win.get_rect(center=(screen_width/2+50, screen_height/2-150))
win_rect2 = win.get_rect(center=(screen_width/2+50, screen_height/2))
win_rect3 = win.get_rect(center=(screen_width/2+50, screen_height/2+150))

lost = pygame.image.load('ressource/text/lost.png')
lost = pygame.transform.scale(lost, (491,188))
lost_rect = lost.get_rect(center=(screen_width/2+50, screen_height/2-150))
lost_rect2 = lost.get_rect(center=(screen_width/2+50, screen_height/2))
lost_rect3 = lost.get_rect(center=(screen_width/2+50, screen_height/2+150))

player_rect1 = player_text.get_rect(center=(screen_width/2-400, screen_height/2-150))
player_rect2 = player_text.get_rect(center=(screen_width/2-400, screen_height/2))
player_rect3 = player_text.get_rect(center=(screen_width/2-400, screen_height/2+150))

number1_rect1 = number1.get_rect(center=(screen_width/2-250, screen_height/2-150))
number2_rect2 = number2.get_rect(center=(screen_width/2-250, screen_height/2))
number3_rect3 = number3.get_rect(center=(screen_width/2-250, screen_height/2+150))

exit_button = pygame.image.load('ressource/button/exit.png')
exit_button = pygame.transform.scale(exit_button, (150,150))
exit_rect = exit_button.get_rect(center=(screen_width/2-125, screen_height/2+250))

reinisalise = pygame.image.load('ressource/button/reinitialise.png')
reinisalise = pygame.transform.scale(reinisalise, (150,150))
reinisalise_rect = reinisalise.get_rect(center=(screen_width/2+125, screen_height/2+250))


background = (15, 157, 232)

running=True
playing=False
nb_player=1
fps=10
player1=True
player2=True
player3=True
player_play=random.randint(1,nb_player)
board_menu=False
number_player=1
win_test=False
player_bot=False

allumette=random.randint(10,20)

#init
def init():
    global background
    screen.fill(background)


#event
def event():
    global running,playing,play_rect,nb_player,right_rect,left_rect,allumette,enter_rect,setting_rect,board_menu
    global number1_rect,number2_rect,number3_rect,circle_rect,number_player,player_play,exit_rect,reinisalise_rect

    click=False

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if not playing and not board_menu:
        if play_rect.collidepoint(mouse_pos) and mouse_click[0] and not board_menu:
            playing=True

    if playing:
        if right_rect.collidepoint(mouse_pos) and mouse_click[0] and not click and nb_player<3 and nb_player<allumette and not board_menu:
            nb_player+=1
            click=True

        if left_rect.collidepoint(mouse_pos) and mouse_click[0] and not click and nb_player>1 and not board_menu:
            nb_player-=1
            click=True

        if enter_rect.collidepoint(mouse_pos) and mouse_click[0] and not click and allumette>=1 and not board_menu:
            for i in range(0,nb_player):
                animation()
                allumette-=1
            if player_play>=number_player:
                player_play=1
            else:
                player_play+=1

    if setting_rect.collidepoint(mouse_pos) and mouse_click[0] and not click:
        if board_menu:
            board_menu=False
        else:
            board_menu=True
        click=True

    if board_menu:
        if number1_rect.collidepoint(mouse_pos) and mouse_click[0]:
            circle_rect = circle.get_rect(center=(screen_width/2-150, screen_height/2))
            number_player=1
            player_play=random.randint(1,number_player)
            click = True

        if number2_rect.collidepoint(mouse_pos) and mouse_click[0] and not click:
            circle_rect = circle.get_rect(center=(screen_width/2, screen_height/2))
            number_player=2
            player_play=random.randint(1,number_player)
            click = True

        if number3_rect.collidepoint(mouse_pos) and mouse_click[0] and not click:
            circle_rect = circle.get_rect(center=(screen_width/2+150, screen_height/2))
            number_player=3
            player_play=random.randint(1,number_player)
            click = True

        if exit_rect.collidepoint(mouse_pos) and mouse_click[0] and not click:
            board_menu=False
            if playing:
                playing=False
            else:
                running=False
            click = True

        if reinisalise_rect.collidepoint(mouse_pos) and mouse_click[0] and not click:
            board_menu=False
            click = True
            réinitialisation()



    if click:
        click=False
        pygame.time.wait(300)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if board_menu:
                    board_menu=False
                elif playing:
                    playing=False
                else:
                    running=False


#interface
def interface():
    global play_button,play_rect
    screen.blit(play_button,play_rect)




#play
def play():
    global allumette,nb_player,enter,enter_rect,number_player,win_test,player1,player2,player3,player_bot,player_play
    global win,win_rect,win_rect2,win_rect3,lost,lost_rect,lost_rect2,lost_rect3
    global player_text,player_rect1,player_rect2,player_rect3
    global number1,number2,number3,number1_rect1,number2_rect2,number3_rect3

    if number_player==1:
        number_player=2
        player_bot=True
        player_play=random.randint(1,2)

    allumette_picture(False)

    number = pygame.image.load('ressource/text/'+str(nb_player)+'.png')
    number = pygame.transform.scale(number, (133,182))
    number_rect = number.get_rect(center=(screen_width/2, screen_height/2+350))
    number_play = pygame.image.load('ressource/text/'+str(player_play)+'.png')
    number_play = pygame.transform.scale(number_play, (133,182))
    number_play_rect = number_play.get_rect(center=(screen_width/2-250, screen_height/2-350))

    player1_text = pygame.image.load('ressource/text/player.png')
    player1_text = pygame.transform.scale(player1_text, (200,80))
    player1_rect = player1_text.get_rect(center=(screen_width/2-500, screen_height/2-350))

    screen.blit(right,right_rect)
    screen.blit(left,left_rect)
    screen.blit(number,number_rect)
    screen.blit(enter,enter_rect)
    screen.blit(player1_text,player1_rect)
    screen.blit(number_play,number_play_rect)

    if nb_player>allumette and nb_player>1:
        nb_player-=1

    if player_play==2 and player_bot:
        pygame.time.wait(1000)
        bot()
        player_play=1

    if allumette<=0:
        if player_play>1:
            player_play-=1
        else:
            player_play=number_player

        if player_play==1:
            player1=False

        elif player_play==2:
            player2=False

        else:
            player3=False
        win_test=True

    if win_test:
        screen.blit(player_text,player_rect1)
        screen.blit(number1,number1_rect1)
        if number_player>=2:
            screen.blit(player_text,player_rect2)
            screen.blit(number2,number2_rect2)
        if number_player>=3:
            screen.blit(player_text,player_rect3)
            screen.blit(number3,number3_rect3)
        if player1:
            screen.blit(win,win_rect)
        else:
            screen.blit(lost,lost_rect)

        if player2 and number_player>=2:
            screen.blit(win,win_rect2)
        else:
            if number_player>=2:
                screen.blit(lost,lost_rect2)

        if player3 and number_player>=3:
            screen.blit(win,win_rect3)
        else:
            if number_player>=3:
                screen.blit(lost,lost_rect3)

#animation
def animation():
    global nb_player,fps
    for i in range(0,8):
        init()
        allumette_button = pygame.image.load('ressource/allumette/'+str(i)+'.png')
        allumette_button = pygame.transform.scale(allumette_button, (250,750))
        allumette_rect = allumette_button.get_rect(center=(screen_width/20, screen_height/2))
        screen.blit(allumette_button,allumette_rect)
        allumette_picture(True)
        pygame.display.flip()
        pygame.time.wait(1000//fps)

def allumette_picture(anim):
    global allumette
    nb=screen_width/20
    a=0
    if anim:
        a=1
        nb+=screen_width/10

    for i in range(a,allumette):
        allumette_button = pygame.image.load('ressource/allumette/0.png')
        allumette_button = pygame.transform.scale(allumette_button, (250,750))
        allumette_rect = allumette_button.get_rect(center=(screen_width/2, screen_height/2))

        allumette_rect = allumette_button.get_rect(center=(nb, screen_height/2))
        screen.blit(allumette_button,allumette_rect)
        nb+=screen_width/10

#settings
def settings():
    global setting,setting_rect,board_menu,menu_board,menu_rect,circle,circle_rect,player_text,player_rect
    global number1,number1_rect,number2,number2_rect,number3,number3_rect,exit_button,exit_rect
    global reinisalise,reinisalise_rect

    screen.blit(setting,setting_rect)

    if board_menu:
        screen.blit(menu_board,menu_rect)
        screen.blit(player_text,player_rect)
        screen.blit(number1,number1_rect)
        screen.blit(number2,number2_rect)
        screen.blit(number3,number3_rect)
        screen.blit(circle,circle_rect)
        screen.blit(exit_button,exit_rect)
        screen.blit(reinisalise,reinisalise_rect)


#bot
def bot():
    global allumette,player_play
    res=0
    if allumette>0:
        if allumette>4:
            res=random.randint(1,3)
        else:
            res=allumette-1
        if res<=0:
                res=1
    if allumette>=1:
        for i in range(0,res):
            animation()
            allumette-=1
    player_play=1

#réinitialisation
def réinitialisation():
    global player1,player2,player3,player_play,win_test,player_bot,allumette
    player1=True
    player2=True
    player3=True
    player_play=random.randint(1,nb_player)
    win_test=False
    player_bot=False

    allumette=random.randint(10,20)


while running:
    init()
    event()

    if playing:
        play()

    else:
        interface()

    settings()

    pygame.display.flip()

pygame.quit()