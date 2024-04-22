from math import acos, degrees
from src.primitives.Triangle import Triangle
from glm import vec3, vec4, normalize

class DirectedProjectile(Triangle):
    def __init__(self, x, y, target):
        super().__init__(
            vec3(x, y, 0), # Position
            vec3(0.5, -0.5, 1), # Scale
            (0, 1, 0) # Color
        )
        aux = normalize(target - self.position)
        self.velocity = 0.25*aux
        self.rotation = vec4(0, 0, 1, -90+degrees(acos(aux.x)))
        self.isEnemy = True
    
    def updatePosition(self):
        self.position += self.velocity 