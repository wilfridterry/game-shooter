import sys
from random import randint
import pygame
from utils.models import Game, GameElement


pygame.init()

game = Game(width=900, height=700, color=(32, 52, 81))
game.display.set_caption("Awesome Shooter Game")
dimentions = (game.screen.get_width(), game.screen.get_height())

fighter = GameElement('Fighter', './images/fighter.png', dimentions)
fighter.move_by_x(game.screen.get_width() / 2 - fighter.width / 2)
fighter.move_by_y(game.screen.get_height() - fighter.height)
fighter.set_step(0.5)

ball = GameElement('Ball', './images/ball.png', dimentions)
ball.set_step(0.3)
ball.hide()

alien = GameElement('Alien', './images/alien.png', dimentions)
alien.set_step(0.1)
alien.set_position(randint(0, game.screen.get_width() - alien.width), 0)

game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and fighter.can_move_left():
                fighter.move_left()
            if event.key == pygame.K_RIGHT and fighter.can_move_right():
                fighter.move_right()
            if event.key == pygame.K_SPACE:
                ball.show()
                ball.move_by_x(fighter.x + fighter.width / 2 - ball.width / 2)
                ball.move_by_y(fighter.y - ball.height)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter.stop_moving_left()
            if event.key == pygame.K_RIGHT:
                fighter.stop_moving_right()

    fighter.keep_moving_left()
    fighter.keep_moving_right()

    alien.move_down()

    if ball.is_visible and ball.is_above_up():
        ball.hide()

    if ball.is_visible:
        ball.move_up()

    game.fill()
    game.blit_element(fighter)
    game.blit_element(alien)

    if ball.is_visible:
        game.blit_element(ball)

    game.display.update()

    if alien.is_under_down():
        game_is_running = False

game_over_text = game.font.render("Game Over", True, "white")
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (game.screen.get_width() / 2, game.screen.get_height() / 2)
game.screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()