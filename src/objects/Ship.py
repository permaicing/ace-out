from OpenGL.GL import *
from src.primitive.Triangle import Triangle
from src.objects.Projectil import Projectil
import glm

class Ship(Triangle):
    def __init__(self):
        super().__init__(
            glm.vec3(0, -8, 0), # Position
            glm.vec3(2, 2, 1), # Scale
            (0, 0, 1) # Color
        )
        self.velocity = glm.vec3(0.2, 0, 0)
        self.fireRate = 100
        self.fireRateCheio = 100
    
    def updatePosition(self, game):
        if game.direita and self.position.x <= game.mundoLar/2-1.15:
            self.position += self.velocity
            
        if game.esquerda and self.position.x >= -game.mundoLar/2+1.15:
            self.position -= self.velocity

    def atirar(self, game):
        if self.fireRate <= 0:
            game.projectiles.append(
                Projectil(self.position.x, self.position.y+1, False)
            )
            self.fireRate = self.fireRateCheio