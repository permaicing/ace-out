from src.primitives.Triangle import Triangle
from src.objects.Projectile import Projectile
from src.textures.Texture import Texture
from src.objects.Mesh import Mesh
import glm

class Ship(Mesh):
    def __init__(self, objFilepath, mtlFilepath, correctionAngle=45):
        ambient = glm.vec3(0.1, 0.1, 0.5)
        diffuse = glm.vec3(0.2, 0.2, 0.8)
        specular = glm.vec3(1.0, 1.0, 1.0)
        shine = 16.0
        super().__init__(objFilepath, mtlFilepath, shading_frequency=1, ambient=ambient, diffuse=diffuse, specular=specular, shine=shine)
        self.position = glm.vec3(0, -8, 0)
        self.scale = glm.vec3(0.35, 0.35, 0.35)
        self.rotation = glm.vec4(0, 1, 0, 0)
        self.velocity = 0.2 * glm.vec3(1, 0, 0)
        self.fireGauge = 100
        self.fireGaugeFull = 100
    
    def updatePosition(self, game):
        if game.right and self.position.x <= game.sceneW:
            self.position += self.velocity
            self.rotation.w += 5
        if game.left and self.position.x >= -game.sceneW:
            self.position -= self.velocity
            self.rotation.w -= 5
        else:
            aux = abs(self.rotation.w)
            if aux % 360 != 0:
                mod = 1 if aux <= 180 else -1
                self.rotation.w -= mod*(aux/self.rotation.w)

    def fire(self, game):
        if self.fireGauge <= 0:
            game.projectiles.append(
                Projectile(self.position.x, self.position.y+1, False)
            )
            self.fireGauge = self.fireGaugeFull

    def draw(self, game):
        super().draw(game)