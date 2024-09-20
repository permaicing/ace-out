from src.primitives.Triangle import Triangle
from src.objects.Projectile import Projectile
from src.textures.Texture import Texture
from src.objects.Mesh import Mesh
import glm

class Ship(Mesh):
    def __init__(self, objFilepath, mtlFilepath):
        super().__init__(objFilepath, mtlFilepath)
        self.position = glm.vec3(0, -8, 0)
        self.scale = glm.vec3(0.35, 0.35, 0.35)
        self.rotation = glm.vec4(1, 0, 0, 45)
        self.velocity = 0.2 * glm.vec3(1, 0, 0)
        self.fireGauge = 100
        self.fireGaugeFull = 100
    
    def updatePosition(self, game):
        if game.right and self.position.x <= game.sceneW:
            self.position += self.velocity
            
        if game.left and self.position.x >= -game.sceneW:
            self.position -= self.velocity

    def fire(self, game):
        if self.fireGauge <= 0:
            game.projectiles.append(
                Projectile(self.position.x, self.position.y+1, False)
            )
            self.fireGauge = self.fireGaugeFull