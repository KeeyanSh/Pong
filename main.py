import sys
import time
from Player import *
from game import Game

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Pong')
GREEN = (75, 150, 100)
ball = pygame.draw.circle(screen, (255, 255, 0), (400, 350), 17)
player = HumanPlayer(screen)
bot = BotPlayer(screen, ball)
game = Game(screen, player.rect, bot.rect, ball)

isPaused = False
while True:
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        isPaused = not isPaused
        game.pause()
        time.sleep(.2)

    if pygame.event.poll().type == pygame.QUIT:
        sys.exit()

    if isPaused:
        continue
    screen.fill((0, 25, 20))

    pygame.draw.rect(screen, GREEN, (400, 0, 1, 700), 0)
    player.handle_keys()
    bot.handle(game.ballDirection[0])
    game.move_ball()
    pygame.display.update()
