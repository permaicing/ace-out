from OpenGL.GL import *
from src.primitives.Triangle import Triangle
from src.objects.Projectile import Projectile
import glm

class Ship(Triangle):
    def __init__(self):
        super().__init__(
            glm.vec3(0, -8, 0), # Position
            glm.vec3(2, 2, 1), # Scale
            (0, 0, 1) # Color
        )
        self.velocity = glm.vec3(0.2, 0, 0)
        self.fireGauge = 100
        self.fireGaugeFull = 100
    
    def updatePosition(self, game):
        if game.right and self.position.x <= game.sceneW/2-1.15:
            self.position += self.velocity
            
        if game.left and self.position.x >= -game.sceneW/2+1.15:
            self.position -= self.velocity

    def fire(self, game):
        if self.fireGauge <= 0:
            game.projectiles.append(
                Projectile(self.position.x, self.position.y+1, False)
            )
            self.fireGauge = self.fireGaugeFull