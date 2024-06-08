import pygame
import time
import random

pygame.init()

# Definición de colores
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)

# Dimensiones de la pantalla y del área de juego
dis_width = 800
dis_height = 600
game_area_width = dis_width - 40
game_area_height = dis_height - 80

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Configuración del reloj y del tamaño de la serpiente
clock = pygame.time.Clock()
snake_block = 25  # Tamaño del bloque de la serpiente
snake_speed = 15

# Fuentes para el estilo del texto y el puntaje
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Margen superior para el puntaje
score_margin_top = 30

# Función para dibujar la serpiente
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

# Función para mostrar el puntaje
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [(dis_width - value.get_width()) // 2, score_margin_top])

# Función para mostrar mensajes en la pantalla
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    x1 = (dis_width - game_area_width) // 2 + game_area_width // 2
    y1 = (dis_height - game_area_height) // 2 + game_area_height // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange((dis_width - game_area_width) // 2, (dis_width + game_area_width) // 2 - snake_block) / snake_block) * snake_block
    foody = round(random.randrange((dis_height - game_area_height) // 2, (dis_height + game_area_height) // 2 - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= (dis_width + game_area_width) // 2 or x1 < (dis_width - game_area_width) // 2 or y1 >= (dis_height + game_area_height) // 2 or y1 < (dis_height - game_area_height) // 2:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        
        # Dibujar el borde del área de juego
        pygame.draw.rect(dis, white, [(dis_width - game_area_width) // 2, (dis_height - game_area_height) // 2, game_area_width, game_area_height], 2)

        # Dibujar la comida
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Comprobar si la serpiente choca consigo misma
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Comprobar si la serpiente ha comido la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange((dis_width - game_area_width) // 2, (dis_width + game_area_width) // 2 - snake_block) / snake_block) * snake_block
            foody = round(random.randrange((dis_height - game_area_height) // 2, (dis_height + game_area_height) // 2 - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
