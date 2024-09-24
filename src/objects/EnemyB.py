from random import uniform
from src.primitives.Eneagon import Eneagon
from src.objects.Projectile import Projectile
from src.objects.Mesh import Mesh
from glm import vec3, normalize, vec4
from math import degrees, acos
import glm

class EnemyB(Mesh):
    def __init__(self, x, objFilepath="src/models/enemies/enemyB.obj", mtlFilepath="src/models/enemies/enemyB.mtl"):
        ambient = glm.vec3(0.0, 0.2, 0.0)
        diffuse = glm.vec3(0.0, 0.8, 0.0)
        specular = glm.vec3(1.0, 1.0, 1.0)
        shine = 16.0
        super().__init__(objFilepath, mtlFilepath, ambient=ambient, diffuse=diffuse, specular=specular, shine=shine)
        self.position = vec3(x, 12, 0)
        self.scale = vec3(1, 1, 1)
        self.rotation = vec4(0, 0, 1, 0)
        aux = normalize(vec3(uniform(-1, 1), -1, 0))
        self.velocity = 0.05 * aux
        self.rotation.w = 90 - degrees(acos(aux.x))
        self.fireGauge = 0
        self.fireGaugeFull = 200
        
    def updatePosition(self):
        # self.scale.x += self.scale_delta
        # self.scale.y += self.scale_delta
        # if self.scale.x >= 2 or self.scale.x <= 0.9:
        #     self.scale_delta *= -1
        self.position += self.velocity
        
    def fire(self, game):
        if self.fireGauge <= 0:
            game.projectiles.append(
                Projectile(self.position.x, self.position.y, True)
            )
            self.fireGauge = self.fireGaugeFull

    def draw(self, game):
        super().draw(game)