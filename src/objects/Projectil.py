from src.primitive.Triangle import Triangle
import glm

class Projectil(Triangle):
    def __init__(self, posX, isEnemy):
        self.vecPosition = glm.vec3(posX, -7, 0)
        self.vecScale = glm.vec3(0.5, 0.5, 1)
        self.deslocamento = glm.vec3(0, 1, 0)
        self.velocDeslocamento = 0.3
        self.isEnemy = isEnemy
        self.color = [0, 1, 0]
        super().__init__(
            self.vecPosition, self.vecScale, self.deslocamento, self.velocDeslocamento, self.color
        )
    
    def updatePosition(self):
        if self.isEnemy:
            self.position = self.position - self.velocDeslocamento * self.deslocamento
        else:
            self.position = self.position + self.velocDeslocamento * self.deslocamento  
            