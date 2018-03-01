import sys
import random
import pygame

pygame.init()

cell_width = 20
cols, rows = 50, 50
width, height = cols * cell_width, rows * cell_width

screen = pygame.display.set_mode((width, height))

snake = [(cols // 2 - 1, rows // 2), (cols // 2, rows // 2)]
food = None
speed = (1, 0)

clock = pygame.time.Clock()

def create_rectange(pos):
    lu = pos[0] * cell_width, pos[1] * cell_width
    ru = (pos[0] + 1) * cell_width, pos[1] * cell_width
    rl = (pos[0] + 1) * cell_width, (pos[1] + 1) * cell_width
    ll = pos[0] * cell_width, (pos[1] + 1) * cell_width    

    return [lu, ru, rl, ll]

def draw():

    for x, y in snake:
        if ((x, y) == snake[0]):
            pygame.draw.polygon(screen, (0, 180, 0), create_rectange((x, y)), 0)
        else:
            pygame.draw.polygon(screen, (0, 255, 0), create_rectange((x, y)), 0)

    pygame.draw.polygon(screen, (255, 0, 0), create_rectange(food), 0)

def move_snake():
    global snake

    snake.pop()
    snake.insert(0, (snake[0][0] + speed[0], snake[0][1] + speed[1]))
    

def get_empty():
    empty_squares = []

    for y in range(rows):
        for x in range(cols):
            if (x, y) not in snake:
                empty_squares.append((x, y))

    return empty_squares

def put_food():
    global food
    food = random.choice(get_empty())

put_food()
print(food)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                speed = (1, 0)
            elif event.key == pygame.K_UP:
                speed = (0, -1)
            if event.key == pygame.K_DOWN:
                speed = (0, 1)

    screen.fill((255, 255, 255))
    clock.tick(5)

    move_snake()

    if snake[0] == food:
        snake.append(food)
        put_food()
    elif snake[0] in snake[1:]:
        print("Game Over.")

    draw()
    pygame.display.flip()