import pygame
from random import *
import time

from pygame import display
from pygame.sprite import DirtySprite

def setup(level):
    
    global display_time

    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)

    number_count = (level // 3)+5
    number_count = min(number_count,20)

    shuffle_grid(number_count)

def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110

    screen_left_margin = 55 #스크린 여백용
    screen_top_margin = 20


    grid = [[0 for col in range(columns)] for row in range(rows)]
    number = 1
    while number <= number_count:
        row_idx = randrange(0,rows)
        column_idx = randrange(0,columns)
        if grid[row_idx][column_idx] == 0 :
            grid[row_idx][column_idx] = number
            number += 1

            center_x = screen_left_margin +(column_idx * cell_size) + (cell_size/2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size/2)

            button = pygame.Rect(0,0,button_size,button_size)
            button.center = (center_x,center_y)

            number_buttons.append(button)
            


def display_start_screen():
    pygame.draw.circle(screen, WHIHE, start_button.center, 60, 5) #화면에,하얀색, 중심좌표,반지름,두께

    msg = game_font.render(f"{curr_level}",True,WHIHE)
    msg_rect = msg.get_rect(center=start_button.center)

    screen.blit(msg,msg_rect)

def display_game_screen():
    global hidden

    if not hidden:
        elapsed_time = (pygame.time.get_ticks()- start_ticks) /1000
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            pygame.draw.rect(screen,WHIHE,rect)
        else:
            cell_text = game_font.render(str(idx),True,WHIHE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)

def check_buttons(pos):
    global start, start_ticks

    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(pos):
    global hidden,curr_level, start
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("Correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else: 
                print("Wrong")
                game_over()
            break

    if len(number_buttons) == 0:
        start =False
        hidden = False
        curr_level += 1
        setup(curr_level)
        
def game_over():
    global running
    running = False
    
    msg = game_font.render(f"Your level is {curr_level}",True,WHIHE)
    msg_rect = msg.get_rect(center=(screen_width/2,screen_height/2))

    screen.fill(BLACK)
    screen.blit(msg,msg_rect)
        

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None,120)

start_button = pygame.Rect(0,0, 120,120)
start_button.center = (120, screen_height - 120)

BLACK = (0,0,0)
WHIHE = (255,255,255)
GRAY = (50,50,50)

number_buttons = []
curr_level = 1
display_time = None
start_ticks = None

start = False
hidden = False

setup(curr_level)

running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()


    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()
    
    if click_pos:
        check_buttons(click_pos)

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
