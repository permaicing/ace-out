from OpenGL.GL import *
from src.primitive.Primitive import Primitive
import glm

class Shield(Primitive):
    def __init__(self, position, scale, color):
        super().__init__(position, scale, color)
    
    def draw(self):
        glPushMatrix()
        super().draw()
        glBegin(GL_POLYGON)
        glVertex2f(0, -0.5)
        glVertex2f(-0.5, -0.25)
        glVertex2f(-0.5, 0.5)
        glVertex2f(-0.25, 0.25)
        glVertex2f(0, 0.5)
        glVertex2f(0.25, 0.25)
        glVertex2f(0.5, 0.5)
        glVertex2f(0.5, -0.25)
        glEnd()
        glPopMatrix()