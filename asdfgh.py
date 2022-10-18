from random import shuffle
from tabnanny import check
import pygame
from random import *

def setup(level):
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    shuffle_grid(number_count)

def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110

    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)
            
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    print(grid)


def display_start_screen():
    pygame.draw.circle(화면, WHITE, start_button.center, 60, 5)

def display_game_screen():
    print("Game Start")

def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

pygame.init()

가로 = 1280
세로 = 720
화면 =pygame.display.set_mode((가로, 세로))
pygame.display.set_caption("메모리게임")

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, 세로 - 120)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

number_buttons = []

start = False

setup(1)

running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)


    화면.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()

    if click_pos:
        check_buttons(click_pos)



    pygame.display.update()

pygame.quit()