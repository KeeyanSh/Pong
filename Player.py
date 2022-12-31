import pygame

GREEN = (75, 150, 100)
YEllOW = (255, 255, 0)


class Player:
    def __init__(self, x, screen):
        self.rect = pygame.rect.Rect((x, 290, 22, 120))
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, self.rect)


class HumanPlayer(Player):
    def __init__(self, screen):
        super().__init__(770, screen)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.y > 5:
            self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN] and self.rect.y < 575:
            self.rect.move_ip(0, 1)
        self.draw()


class BotPlayer(Player):
    def __init__(self, screen, ball):
        super().__init__(8, screen)
        self.ball = ball
        self.count = 0

    def handle(self, x_direction):
        self.draw()
        if x_direction > 0:
            return
        if self.count < 1:
            self.count += 1
            return
        self.count = 0
        if self.ball.y < self.rect.y + 60 and self.rect.y > 5:
            self.rect.move_ip(0, -1)
        elif self.ball.y > self.rect.y + 60 and self.rect.y < 575:
            self.rect.move_ip(0, 1)
