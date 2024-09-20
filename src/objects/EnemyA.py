from src.primitives.Star import Star
from src.objects.Mesh import Mesh
from src.objects.DirectedProjectile import DirectedProjectile
from glm import vec3, vec4

class EnemyA(Mesh):
    def __init__(self, x, objFilepath = "src/models/enemies/enemyA.obj", mtlFilepath = "src/models/enemies/enemyA.mtl"):
        super().__init__(objFilepath, mtlFilepath)
        self.position = vec3(x, 12, 0)
        self.scale = vec3(0.8, 0.8, 0.8)
        self.rotation = vec4(1, 0, 0, 90)
        self.spin = vec4(0, 0, 1, 0)
        self.velocity = 0.05*vec3(0, -1, 0)
        self.fireGauge = 0
        self.fireGaugeFull = 200
        
    def updatePosition(self):
        # self.rotation.w -= 0.5
        # if abs(self.rotation.w) >= 360:
        #     self.rotation.w = 0
        self.position += self.velocity
        #TODO: consertar a rotacao da nave


    def fire(self, game):
        if self.fireGauge <= 0:
            game.projectiles.append(
                DirectedProjectile(self.position.x, self.position.y, game.ship.position)
            )
            self.fireGauge = self.fireGaugeFull