from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import FLY, FLY_TYPE


class Fly(PowerUp):
    def __init__(self):
        self.image = FLY
        self.type = FLY_TYPE
        super().__init__(self.image, self.type)