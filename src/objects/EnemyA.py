from OpenGL.GL import *
from src.primitives.Star import Star
from src.objects.Projectile import Projectile
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
        self.fireGauge = 0
        self.fireGaugeFull = 200
        
    def updatePosition(self):
        self.rotation.w -= 0.5
        if abs(self.rotation.w) >= 360:
            self.rotation.w = 0
        self.position += self.velocity
        
    def fire(self, game):
        if self.fireGauge <= 0:
            game.projectiles.append(
                Projectile(self.position.x, self.position.y, True)
            )
            self.fireGauge = self.fireGaugeFull