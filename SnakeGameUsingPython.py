# importing the necessary modules  
import pygame     
import time      
import random    
  
# defining the speed of the snake  
speed_of_snake = 15  
  
# defining the size of the window  
screen_width = 700  
screen_height = 460  
  
# defining  the colors  
blue = pygame.Color(25, 25, 112)  
mint_cream = pygame.Color(245, 255, 250)  
crimson_red = pygame.Color(220, 20, 60)  
lawn_green = pygame.Color(124, 252, 0)  
orange_red = pygame.Color(255, 69, 0)  
  
# initializing the pygame window using the pygame.init() function  
pygame.init()  

display_screen = pygame.display.set_mode((screen_width, screen_height))  
pygame.display.set_caption('Snake Game By - Dhiraj Kumar (@codeasitis)')  
game_clock = pygame.time.Clock()  
position_of_snake = [100, 50]  
  
# defining the first four blocks of snake body  
body_of_snake = [  
    [100, 50],  
    [90, 50],  
    [80, 50],  
    [70, 50]  
    ]  
  
# position of the fruit  
position_of_fruit = [  
    random.randrange(1, (screen_width//10)) * 10,  
    random.randrange(1, (screen_height//10)) * 10  
    ]  
spawning_of_fruit = True  
  
# setting the default direction of the snake towards RIGHT  
initial_direction = 'RIGHT'  
snake_direction = initial_direction  
  
# initial score  
player_score = 0  
  
# defining the functions to display the score 
def display_score(selection, font_color, font_style, font_size):  
    score_font_style = pygame.font.SysFont(font_style, font_size)  
    score_surface = score_font_style.render('Your Score : ' + str(player_score), True, font_color)  
    score_rectangle = score_surface.get_rect()  
    display_screen.blit(score_surface, score_rectangle)  
  
# function to over the game  
def game_over():  
    game_over_font_style = pygame.font.SysFont('times new roman', 50)  
    game_over_surface = game_over_font_style.render('Your Score is : ' + str(player_score), True, crimson_red )  
    game_over_rectangle = game_over_surface.get_rect()  
    game_over_rectangle.midtop = (screen_width/2, screen_height/4)  
    # displaying the text on the screen  
    display_screen.blit(game_over_surface, game_over_rectangle)  
    pygame.display.flip()  
    time.sleep(2)  
    pygame.quit()  
    quit()  
  
# setting the run flag value to True  
game_run = True  
  
# the game loop  
# using the while loop  
while game_run:  
    # iterating through the events in the pygame.event module  
    for event in pygame.event.get():  
        # setting the variable value to False if the event's type is equivalent to pygame's QUIT constant  
        if event.type == pygame.QUIT:  
            # setting the flag value to False  
            game_run = False  
  
        # setting the variable value either to UP, DOWN, LEFT, or RIGHT  
        # if the event's type is equivalent to pygame's KEYDOWN constant,  
        # and any of the stated keys is pressed  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP:  
                snake_direction = 'UP'  
            if event.key == pygame.K_DOWN:  
                snake_direction = 'DOWN'  
            if event.key == pygame.K_LEFT:  
                snake_direction = 'LEFT'  
            if event.key == pygame.K_RIGHT:  
                snake_direction = 'RIGHT'  
  
    # neglecting the action taken if the key of opposite direction is pressed  
    if snake_direction == 'UP' and initial_direction != 'DOWN':  
        initial_direction = 'UP'  
    if snake_direction == 'DOWN' and initial_direction != 'UP':  
        initial_direction = 'DOWN'   
    if snake_direction == 'LEFT' and initial_direction != 'RIGHT':  
        initial_direction = 'LEFT'   
    if snake_direction == 'RIGHT' and initial_direction != 'LEFT':  
        initial_direction = 'RIGHT'  
  
    # updating the position of the snake for every direction   
    if initial_direction == 'UP':  
        position_of_snake[1] -= 10  
    if initial_direction == 'DOWN':  
        position_of_snake[1] += 10  
    if initial_direction == 'LEFT':  
        position_of_snake[0] -= 10  
    if initial_direction == 'RIGHT':  
        position_of_snake[0] += 10  
      
    # updating the body of the snake  
    body_of_snake.insert(0, list(position_of_snake))  
    if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:  
        # incrementing the player's score by 1  
        player_score += 1  
        spawning_of_fruit = False  
    else:  
        body_of_snake.pop()  
  
    # randomly spawning the fruit  
    if not spawning_of_fruit:  
        position_of_fruit = [  
            random.randrange(1, (screen_width//10)) * 10,  
            random.randrange(1, (screen_height//10)) * 10  
        ]  
    spawning_of_fruit = True  
  
    # filling the color on the screen  
    display_screen.fill(mint_cream)  
  
    # drawing the game objects on the screen  
    for position in body_of_snake:  
        pygame.draw.rect(display_screen, lawn_green, pygame.Rect(position[0], position[1], 10, 10))  
        pygame.draw.rect(display_screen, orange_red, pygame.Rect(position_of_fruit[0], position_of_fruit[1], 10, 10))  
  
    # conditions for the game to over  
    if position_of_snake[0] < 0 or position_of_snake[0] > screen_width - 10:  
        game_over()  
    if position_of_snake[1] < 0 or position_of_snake[1] > screen_height - 10:  
        game_over()      
  
    # touching the snake body  
    for block in body_of_snake[1:]:  
        if position_of_snake[0] == block[0] and position_of_snake[1] == block[1]:  
            game_over  
  
    # displaying the score continuously  
    display_score(1, blue, 'times new roman', 20)  
  
    # refreshing the game screen  
    pygame.display.update()  
  
    # refresh rate  
    game_clock.tick(speed_of_snake)  
  
# calling the quit() function to quit the application  
pygame.quit()  