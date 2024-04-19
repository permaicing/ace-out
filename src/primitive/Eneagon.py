from math import pi as PI, sin, cos
from OpenGL.GL import *
import glm
import numpy as np

class Eneagon:
    def __init__(self, vecPosition, vecSacale, deslocamento, velocDeslocamento, color, n_sides):
        self.identidade  = glm.mat4(1) 
        self.position = vecPosition
        
        self.scale = glm.scale(self.identidade, vecSacale) 
        self.translate = glm.mat4(1)
        
        self.deslocamento = deslocamento
        self.velocDeslocamento = velocDeslocamento
        
        self.color = color

        self.n_sides = n_sides

    def calcMatrix(self):
        self.translate = glm.translate(self.identidade, self.position)
        transform = self.translate * self.scale
        transform = glm.transpose(transform)
        return transform
    
    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        
        glPushMatrix()
        glMultMatrixf(np.asarray(self.calcMatrix()))
        
        glBegin(GL_POLYGON)        
        for i in range(0, self.n_sides):
            theta = i * (2.0*PI/self.n_sides)
            glVertex2f(cos(theta), sin(theta))
        glEnd()
        
        glPopMatrix()