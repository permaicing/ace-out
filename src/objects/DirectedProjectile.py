from math import acos, degrees
from src.primitives.Rectangle import Rectangle
from src.textures.Texture import Texture
from glm import vec3, vec4, normalize

class DirectedProjectile(Rectangle):
    def __init__(self, x, y, target):

        objectAmbient = vec3(0.1, 0.1, 0.1)
        objectDiffuse = vec3(0.6, 0.6, 0.6)
        objectSpecular = vec3(1.0, 1.0, 1.0)
        objectShine = 32


        super().__init__(
            vec3(x, y, 0),               
            vec3(0.25, -0.5, 1),         
            (1, 0.7, 0.7),                
            objectAmbient,               
            objectDiffuse,               
            objectSpecular,              
            objectShine,                 
            Texture.texs['bullet'].texId 
        )

        aux = normalize(target - self.position)
        self.velocity = 0.25 * aux

        self.rotation = vec4(0, 0, 1, -90 + degrees(acos(aux.x)))

        self.isEnemy = True  
    
    def updatePosition(self):
        self.position += self.velocity
