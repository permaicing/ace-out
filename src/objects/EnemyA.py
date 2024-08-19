from src.primitives.Star import Star
from src.objects.DirectedProjectile import DirectedProjectile
from glm import vec3

class EnemyA(Star):
    def __init__(self, x):
        super().__init__(
            vec3(x, 12, 0), # Position
            vec3(1.5, 1.5, 1), # Scale
            (1, 0, 0), # Color
            5 # N_corners
        )
        self.velocity = 0.05*vec3(0, -1, 0)
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
                DirectedProjectile(self.position.x, self.position.y, game.ship.position)
            )
            self.fireGauge = self.fireGaugeFull