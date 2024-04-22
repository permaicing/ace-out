from src.primitives.Triangle import Triangle
import glm

class DirectedProjectile(Triangle):
    def __init__(self, x, y, target):
        super().__init__(
            glm.vec3(x, y, 0), # Position
            glm.vec3(0.5, -0.5, 1), # Scale
            (0, 1, 0) # Color
        )
        self.velocity = 0.25*glm.normalize(target - self.position)
        self.isEnemy = True
    
    def updatePosition(self):
        self.position += self.velocity 