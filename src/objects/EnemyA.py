from OpenGL.GL import *
from src.primitive.Star import Star
from src.objects.Projectil import Projectil
import glm

class EnemyA(Star):
    def __init__(self, x):
        super().__init__(
            glm.vec3(x, 8, 0), # Position
            glm.vec3(1.5, 1.5, 1), # Scale
            (1, 0, 0), # Color
            5 # N_corners
        )
        self.velocity = glm.vec3(0, -0.05, 0)
        self.fireRate = 0
        self.fireRateCheio = 100
        
    def updatePosition(self):
        self.rotation.w -= 0.5 # 1 deg = 0.01745 rad
        if abs(self.rotation.w) >= 360:
            self.rotation.w = 0
        self.position += self.velocity
        
    def atirar(self, game):
        if self.fireRate <= 0:
            game.projectiles.append(
                Projectil(self.position.x, self.position.y, True)
            )
            self.fireRate = self.fireRateCheio