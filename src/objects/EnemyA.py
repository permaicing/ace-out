from OpenGL.GL import *
from src.primitive.Star import Star
from src.objects.Projectil import Projectil
import glm

class EnemyA(Star):
    def __init__(self, x):
        self.vecPosition = glm.vec3(x, 10, 0)
        self.vecScale = glm.vec3(2, 2, 1)
        self.deslocamento = glm.vec3(0, -1, 0)
        self.velocDeslocamento = 0.05
        self.color = [1, 0, 0]
        self.fireRate = 0
        self.fireRateCheio = 100
        
        super().__init__(
            self.vecPosition, self.vecScale, self.deslocamento, self.velocDeslocamento, self.color, 5
        )
        
    def updatePosition(self):
        self.rotation += 1
        self.position = self.position + self.velocDeslocamento * self.deslocamento
        
    def atirar(self, game):
        if self.fireRate <= 0:
            game.projectiles.append(
                Projectil(self.position.x, self.position.y, True)
            )
            self.fireRate = self.fireRateCheio