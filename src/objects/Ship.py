from src.primitives.Triangle import Triangle
from src.objects.Projectile import Projectile
from glm import vec3

class Ship(Triangle):
    def __init__(self):
        super().__init__(
            vec3(0, -8, 0), # Position
            vec3(2, 2, 1), # Scale
            (0, 0, 1) # Color
        )
        self.velocity = 0.2*vec3(1, 0, 0)
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