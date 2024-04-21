from src.primitives.Triangle import Triangle
import glm

class Projectile(Triangle):
    def __init__(self, x, y, isEnemy):
        super().__init__(
            glm.vec3(x, y, 0), # Position
            glm.vec3(0.5, 0.5, 1), # Scale
            (0, 1, 0) # Color
        )
        if isEnemy:
            self.scale.y *= -1
        self.velocity = glm.vec3(0, 1, 0) if not isEnemy else glm.vec3(0, 0.25, 0)
        self.isEnemy = isEnemy
    
    def updatePosition(self):
        if self.isEnemy:
            self.position -= self.velocity
        else:
            self.position += self.velocity 