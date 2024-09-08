from math import pi as PI, sin, cos
from OpenGL.GL import *
from src.primitives.Primitive import Primitive
from glm import vec3

class Projectile(Primitive):
    def __init__(self, x, y, isEnemy):
        super().__init__(vec3(x, y, 0), vec3(0.25, 0.5, 1), (1, 0.7, 0.7) if isEnemy else (1, 1, 1))
        self.isEnemy = isEnemy
        self.depth = 0.1  # Profundidade do projetil
        self.velocity = vec3(0, 1, 0) if not isEnemy else vec3(0, -1, 0)
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glScalef(self.scale.x, self.scale.y, self.depth)
        
        glColor3f(*self.color)  # Define a cor do projetil

        slices = 32  # Número de segmentos do cilindro
        theta = 0.0
        
        # Desenha a lateral do cilindro
        glBegin(GL_QUAD_STRIP)
        for i in range(slices + 1):
            x = cos(theta)
            y = sin(theta)
            glVertex3f(x, y, 0.5)  # Face superior
            glVertex3f(x, y, -0.5)  # Face inferior
            theta += 2.0 * PI / slices
        glEnd()
        
        # Desenha a face superior
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.0, 0.0, 0.5)  # Centro da face superior
        for i in range(slices + 1):
            theta = i * (2.0 * PI / slices)
            glVertex3f(cos(theta), sin(theta), 0.5)
        glEnd()

        # Desenha a face inferior
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.0, 0.0, -0.5)  # Centro da face inferior
        for i in range(slices + 1):
            theta = i * (2.0 * PI / slices)
            glVertex3f(cos(theta), sin(theta), -0.5)
        glEnd()

        glPopMatrix()

    def updatePosition(self):
        self.position += self.velocity
