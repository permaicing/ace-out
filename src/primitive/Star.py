from math import pi as PI, sin, cos, radians
from OpenGL.GL import *
import glm
import numpy as np

class Star:
    def __init__(self, vecPosition, vecSacale, deslocamento, velocDeslocamento, color, n_corners):
        self.identidade  = glm.mat4(1) 
        self.position = vecPosition
        
        self.rotation = 0
        self.scale = glm.scale(self.identidade, vecSacale) 
        self.translate = glm.mat4(1)
        
        self.deslocamento = deslocamento
        self.velocDeslocamento = velocDeslocamento
        
        self.color = color

        self.n_corners = n_corners

    def calcMatrix(self):
        self.translate = glm.translate(self.identidade, self.position)
        transform = self.translate * self.scale
        transform *= glm.rotate(self.identidade, radians(self.rotation), glm.vec3(0, 0, 1))
        transform = glm.transpose(transform)
        return transform
    
    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        
        glPushMatrix()
        glMultMatrixf(np.asarray(self.calcMatrix()))
        
        theta = 0.0
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0.0, 0.0)        
        for i in range(0, self.n_corners+1):
            glVertex2f(cos(theta), sin(theta))
            theta += 2.0*PI/self.n_corners
            glVertex2f(cos(theta)/2.0, sin(theta)/2.0)
            theta += 2.0*PI/self.n_corners
        glEnd()
        
        glPopMatrix()