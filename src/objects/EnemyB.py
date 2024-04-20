from OpenGL.GL import *
from src.primitive.Eneagon import Eneagon
from src.objects.Projectil import Projectil
import glm

class EnemyB(Eneagon):
    def __init__(self, x):
        super().__init__(
            glm.vec3(x, 8, 0), # Position
            glm.vec3(1.5, 1.5, 1), # Scale
            (1, 0, 0), # Color
            6 # N_sides
        )
        self.velocity = glm.vec3(0, -0.05, 0)
        self.scale_delta = 0.01
        self.fireRate = 0
        self.fireRateCheio = 150
        
    def updatePosition(self):
        self.scale.x += self.scale_delta
        self.scale.y += self.scale_delta
        if self.scale.x >= 2 or self.scale.x <= 0.9:
            self.scale_delta *= -1
        self.position += self.velocity
        
    def atirar(self, game):
        if self.fireRate <= 0:
            game.projectiles.append(
                Projectil(self.position.x, self.position.y, True)
            )
            self.fireRate = self.fireRateCheio