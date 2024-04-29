from math import acos, degrees
from src.primitives.Rectangle import Rectangle
from src.textures.Texture import Texture
from glm import vec3, vec4, normalize

class DirectedProjectile(Rectangle):
    def __init__(self, x, y, target):
        super().__init__(
            vec3(x, y, 0), # Position
            vec3(0.25, -0.5, 1), # Scale
            (1, 0.7, 0.7), # Color
            Texture.texs['bullet'].texId
        )
        aux = normalize(target - self.position)
        self.velocity = 0.25*aux
        self.rotation = vec4(0, 0, 1, -90+degrees(acos(aux.x)))
        self.isEnemy = True
    
    def updatePosition(self):
        self.position += self.velocity 