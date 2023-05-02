import random
import pygame
from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.cactus = [SMALL_CACTUS, LARGE_CACTUS]
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(random.choice(self.cactus)))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)