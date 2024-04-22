from src.primitives.Triangle import Triangle
from glm import vec3, normalize

class DirectedProjectile(Triangle):
    def __init__(self, x, y, target):
        super().__init__(
            vec3(x, y, 0), # Position
            vec3(0.5, -0.5, 1), # Scale
            (0, 1, 0) # Color
        )
        self.velocity = 0.25*normalize(target - self.position)
        self.isEnemy = True
    
    def updatePosition(self):
        self.position += self.velocity 