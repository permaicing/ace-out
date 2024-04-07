from OpenGL.GL import *
import glm
import numpy as np

class Triangle:
    def __init__(self, vecPosition, vecSacale, deslocamento, velocDeslocamento, color):
        self.identidade  = glm.mat4(1) 
        self.position = vecPosition
        
        self.scale = glm.scale(self.identidade, vecSacale) 
        self.translate = glm.mat4(1)
        
        self.deslocamento = deslocamento
        self.velocDeslocamento = velocDeslocamento
        
        self.color = color
        
    def calcMatrix(self):
        self.translate = glm.translate(self.identidade, self.position)
        transform = self.translate * self.scale
        transform = glm.transpose(transform)
        return transform
    
    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        
        glPushMatrix()
        glMultMatrixf(np.asarray(self.calcMatrix()))
        
        glBegin(GL_TRIANGLES)        
        glVertex2f(-0.5, -0.5)
        glVertex2f(0, 0.5)
        glVertex2f(0.5, -0.5)
        glEnd()
        
        glPopMatrix()