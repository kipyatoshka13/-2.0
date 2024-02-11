import pygame

screen_height = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
game = True
game_stage = "enter_size"
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
game_size = ""
game_field = {}

def draw_text(text):
    text_draw = my_font.render(text, False, (0, 0, 0))
    screen.blit(text_draw, (100, 100))

def button_to_text(button):
    if button == pygame.K_1:
        text = "1"
    elif button == pygame.K_2:
        text = "2"
    elif button == pygame.K_3:
        text = "3"
    elif button == pygame.K_4:
        text = "4"
    elif button == pygame.K_5:
        text = "5"
    elif button == pygame.K_6:
        text = "6"
    elif button == pygame.K_7:
        text = "7"
    elif button == pygame.K_8:
        text = "8"
    elif button == pygame.K_9:
        text = "9"
    elif button == pygame.K_0:
        text = "0"
    elif button == pygame.K_x:
        text = "x"
    return text



while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                             pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
                             pygame.K_9, pygame.K_0, pygame.K_x, ]:
                if game_stage == "enter_size":
                    text = button_to_text(event.key)
                    if len(game_size) < 5:
                        game_size += text
            elif event.key == pygame.K_BACKSPACE:
                game_size = game_size[:len(game_size)-1]

            elif event.key in [pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s]:
                if event.key == pygame.K_w:
                    snake_coords = snake_pos.split("_")
                    snake_x = int(snake_coords[0])
                    snake_y = int(snake_coords[1])
                    old_snake_coords = str(snake_x) + "_" + str(snake_y)
                    snake_y -= 1
                    new_snake_coords = str(snake_x)+"_"+str(snake_y)
                    game_field[new_snake_coords] = "snake"
                    game_field[old_snake_coords] = "empty"
                    snake_pos = new_snake_coords
                if event.key == pygame.K_s:
                    snake_coords = snake_pos.split("_")
                    snake_x = int(snake_coords[0])
                    snake_y = int(snake_coords[1])
                    old_snake_coords = str(snake_x) + "_" + str(snake_y)
                    snake_y += 1
                    new_snake_coords = str(snake_x)+"_"+str(snake_y)
                    game_field[new_snake_coords] = "snake"
                    game_field[old_snake_coords] = "empty"
                    snake_pos = new_snake_coords
                if event.key == pygame.K_a:
                    snake_coords = snake_pos.split("_")
                    snake_x = int(snake_coords[0])
                    snake_y = int(snake_coords[1])
                    old_snake_coords = str(snake_x) + "_" + str(snake_y)
                    snake_x -= 1
                    new_snake_coords = str(snake_x)+"_"+str(snake_y)
                    game_field[new_snake_coords] = "snake"
                    game_field[old_snake_coords] = "empty"
                    snake_pos = new_snake_coords
                if event.key == pygame.K_d:
                    snake_coords = snake_pos.split("_")
                    snake_x = int(snake_coords[0])
                    snake_y = int(snake_coords[1])
                    old_snake_coords = str(snake_x) + "_" + str(snake_y)
                    snake_x += 1
                    new_snake_coords = str(snake_x)+"_"+str(snake_y)
                    game_field[new_snake_coords] = "snake"
                    game_field[old_snake_coords] = "empty"
                    snake_pos = new_snake_coords





            elif event.key == pygame.K_RETURN:
                game_stage = "prepare_field"
                game_size_final = game_size.split("x")
                game_size_final = [int(game_size_final[0]), int(game_size_final[1])]

                if game_size_final[0] > game_size_final[1]:
                    box_size = screen_width / game_size_final[0]
                else:
                    box_size = screen_height / game_size_final[1]

                x_count = 0
                y_count = 0
                while y_count < game_size_final[1]:
                    x_count = 0
                    while x_count < game_size_final[0]:
                        game_field[str(x_count)+"_"+str(y_count)] = "empty"
                        x_count += 1
                    y_count += 1
                game_field["0_3"] = "snake"
                snake_pos = "0_3"
                snakehead = pygame.image.load("snakehead.png")
                snakehead = pygame.transform.scale(snakehead, (50, 50))


    screen.fill("green")
    #pygame.draw.rect(screen, (21, 13, 238), (285, 285, 30, 30))
    if game_stage == "prepare_field":
        border_w = 2
        if box_size >= 100:
            border_w = 5
        elif box_size > 50 and box_size < 100:
            border_w = 3
        else:
            border_w = 1
        y_count = 0
        while y_count < game_size_final[1]:
            x_count = 0
            while x_count < game_size_final[0]:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (x_count*box_size, y_count*box_size,
                                  box_size, box_size), border_w)
                x_count += 1
            y_count += 1

        y_count = 0
        while y_count < game_size_final[1]:
            x_count = 0
            while x_count < game_size_final[0]:
                if game_field[str(x_count)+"_"+str(y_count)] == "snake":
                    screen.blit(snakehead, (box_size*x_count, box_size*y_count))
                x_count += 1
            y_count += 1


    if game_stage == "enter_size":
        draw_text(game_size)


    pygame.display.update()

