from OpenGL.GL import *
from src.primitive.Triangle import Triangle
from src.objects.Projectil import Projectil
import glm

class Ship(Triangle):
    def __init__(self):
        self.vecPosition = glm.vec3(0, -8, 0)
        self.vecScale = glm.vec3(2, 2, 1)
        self.deslocamento = glm.vec3(1, 0, 0)
        self.velocDeslocamento = 0.2
        self.color = [0, 0, 1]
        self.fireRate = 0
        self.fireRateCheio = 100
        
        super().__init__(
            self.vecPosition, self.vecScale, self.deslocamento, self.velocDeslocamento, self.color
        )
        
    def updatePosition(self, game):
        if game.direita and self.position.x <= game.mundoLar/2:
            self.position = self.position + self.velocDeslocamento * self.deslocamento
            
        if game.esquerda and self.position.x >= -game.mundoLar/2:
            self.position = self.position - self.velocDeslocamento * self.deslocamento

    def atirar(self, game):
        if self.fireRate <= 0:
            game.projectiles.append(
                Projectil(self.position.x, False)
            )
            self.fireRate = self.fireRateCheio