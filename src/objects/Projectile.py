from src.primitives.Triangle import Triangle
from glm import vec3

class Projectile(Triangle):
    def __init__(self, x, y, isEnemy): 
        super().__init__(
            vec3(x, y, 0), # Position
            vec3(0.5, 0.5, 1), # Scale
            (0, 1, 0) # Color
            # Texture('src/textures/bullets/bullet.png')
        )
        if isEnemy:
            self.scale.y *= -1
        self.velocity = 1*vec3(0, 1, 0) if not isEnemy else -0.25*vec3(0, 1, 0)
        self.isEnemy = isEnemy
    
    def updatePosition(self):
        self.position += self.velocity 