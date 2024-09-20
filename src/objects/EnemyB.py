from random import uniform
from src.primitives.Eneagon import Eneagon
from src.objects.Projectile import Projectile
from src.objects.Mesh import Mesh
from glm import vec3, normalize, vec4

class EnemyB(Mesh):
    def __init__(self, x, objFilepath = "src/models/enemies/enemyB.obj", mtlFilepath = "src/models/enemies/enemyB.mtl"):
        super().__init__(objFilepath, mtlFilepath)
        self.position = vec3(x, 12, 0) #colisao so esta contando na asa esquerda para esse unimigo
        self.scale = vec3(1, 1, 1)
        self.rotation = vec4(1, 0, 0, 90)
        self.velocity = 0.05*normalize(vec3(uniform(-1, 1), -1, 0))
        self.scale_delta = 0.01
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