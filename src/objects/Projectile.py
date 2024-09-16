from src.primitives.Rectangle import Rectangle
from src.textures.Texture import Texture
from glm import vec3
import glm

class Projectile(Rectangle):
    def __init__(self, x, y, isEnemy): 
        super().__init__(
            vec3(x, y, 0), # Position
            vec3(0.25, 0.5, 1), # Scale
            (1, 1, 1) if not isEnemy else (1, 0.7, 0.7), # Color

            glm.vec3(0.1, 0.1, 0.1),
            glm.vec3(0.6, 0.6, 0.6),
            glm.vec3(1.0, 1.0, 1.0),
            32,

            Texture.texs['bullet'].texId
        )
        if isEnemy:
            self.scale.y *= -1
        self.velocity = 1*vec3(0, 1, 0) if not isEnemy else -0.25*vec3(0, 1, 0)
        self.isEnemy = isEnemy
    
    def updatePosition(self):
        self.position += self.velocity 