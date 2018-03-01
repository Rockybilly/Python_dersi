import sys
import random
import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

cell_width = 100
cols, rows = 5, 5
width, height = cols * cell_width, rows * cell_width

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake = []
food = (3, 3)

def draw_grid():
    for x in range(0, width + 1, cell_width):
        pygame.draw.line(screen, BLACK, [x, 0], [x, height], 1)

    for y in range(0, height + 1, cell_width):
        pygame.draw.line(screen, BLACK, [0, y], [width, y], 1)

def create_rect(pos):
    #This function takes matrix coordinates.
    
    x, y = pos

    lu = x * cell_width      , y * cell_width
    ru = (x + 1) * cell_width, y * cell_width
    rl = (x + 1) * cell_width, (y + 1) * cell_width
    ll = x * cell_width      , (y + 1) * cell_width

    return [lu, ru, rl, ll]

def get_empty_cells():
    result = []
    for x in range(cols):
        for y in range(rows):
            if (x, y) not in snake:
                result.append((x, y))

    return result

def draw_food():
    pygame.draw.polygon(screen, RED, create_rect(food), 0)

while True:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    draw_grid()
    draw_food()
    pygame.display.flip()
