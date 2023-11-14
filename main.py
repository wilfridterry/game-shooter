import sys
import pygame
from utils.models import GameElement


pygame.init()

screen_width, screen_height = 900, 700
screen_dimentions = (screen_width, screen_height)
screen_fill_color = (32, 52, 81)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

fighter = GameElement('Fighter', './images/fighter.png', screen_dimentions)
fighter.move_by_x(screen_width / 2 - fighter.width / 2)
fighter.move_by_y(screen_height - fighter.height)
fighter.set_step(0.5)

rocket = GameElement('Rocket', './images/rocket.png', screen_dimentions)
rocket.move_by_x(fighter.x + fighter.width / 2 - rocket.width / 2)
rocket.move_by_y(fighter.y - rocket.height)
rocket.hide()

# alien = GameElement('Alien', './images/alien.png', screen_dimentions)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and fighter.can_move_left():
                fighter.move_left()
            if event.key == pygame.K_RIGHT and fighter.can_move_right():
                fighter.move_right()
            if event.key == pygame.K_SPACE:
                rocket.show()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter.stop_moving_left()
            if event.key == pygame.K_RIGHT:
                fighter.stop_moving_right()

    fighter.keep_moving_left()
    fighter.keep_moving_right()

    screen.fill(screen_fill_color)
    screen.blit(fighter.image, (fighter.x, fighter.y))
    if rocket.is_visible:
        screen.blit(rocket.image, (rocket.x, rocket.y))

    pygame.display.update()