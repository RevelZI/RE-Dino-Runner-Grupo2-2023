import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    BIRD_HEIGHTS = (250, 290, 200)
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.index = 0

    def draw(self, screen):
        if self.index >= 10:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1

 