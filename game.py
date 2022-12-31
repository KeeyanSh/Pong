import random
import time
import pygame
from math import *


class Game:
    def __init__(self, screen, r_player, l_player, ball):
        self.screen = screen
        self.r_player = r_player
        self.l_player = l_player
        self.ball = ball
        self.count = self.r_goals = self.l_goals = 0
        self.initialize_ball_directions()
        while self.ballDirection[0] == 0:
            self.ballDirection[0] = random.randint(0, 2)
        pygame.font.init()

    def initialize_ball_directions(self):
        x = random.uniform(2.5, 3.5)
        self.ballDirection = [copysign(x, random.randint(-1, 1)), copysign(sqrt(25 - pow(x, 2)), random.randint(-1, 1))]

    def move_ball(self):
        self.results_view()
        self.check_goal()
        if self.count < 3:
            self.count += 1
        else:
            self.count = 0
            self.check_ball_limits()
            self.ball.move_ip(self.ballDirection[0], self.ballDirection[1])
        pygame.draw.ellipse(self.screen, (255, 255, 0), self.ball)

    def check_ball_limits(self):
        ball = self.ball
        player = None

        if ball.y < 27 or ball.y > 673:
            self.ballDirection[1] *= -1
        elif fabs(ball.x - 736) <= 4 and self.r_player.y - 20 <= ball.y <= self.r_player.y + 112:
            player = self.r_player
        elif fabs(ball.x - 30) <= 4 and self.l_player.y - 20 <= ball.y <= self.l_player.y + 112:
            player = self.l_player
        if player is None:
            return

        self.ballDirection[0] *= -1
        self.set_y_direction(player)

    def set_y_direction(self, player):
        distance = self.ball.y - (player.y + 46)
        self.ballDirection[1] = copysign(fabs(distance) / 46 * 2.5, distance)
        sign = -1 if self.ballDirection[0] < 0 else 1
        self.ballDirection[0] = sign * sqrt(25 - pow(self.ballDirection[1], 2))

    def check_goal(self):
        if not -20 < self.ball.x < 820:
            if self.ball.x < -20:
                self.r_goals += 1
            else:
                self.l_goals += 1
            self.initialize_ball_directions()
            self.ball.x = 400
            self.ball.y = 350
            self.r_player.x = 770
            self.l_player.x = 8
            self.r_player.y = self.l_player.y = 290

            font = pygame.font.SysFont('Comic Sans MS', 130)
            text = font.render('>> GOAL <<', False, (255, 255, 0))
            self.screen.fill((0, 25, 20))
            self.screen.blit(text, (90, 240))
            pygame.display.update()
            time.sleep(1)

    def results_view(self):
        font = pygame.font.SysFont('Comic Sans MS', 40)
        text = font.render(str(self.l_goals) + " " + str(self.r_goals), False, (75, 150, 100))
        self.screen.blit(text, (370, 315))

    def pause(self):
        font = pygame.font.SysFont('Comic Sans MS', 110)
        text = font.render('- Paused -', False, (255, 255, 255))
        self.screen.blit(text, (140, 10))
        pygame.display.update()
