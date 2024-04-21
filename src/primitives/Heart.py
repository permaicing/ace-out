from OpenGL.GL import *
from src.primitives.Primitive import Primitive

class Heart(Primitive):
    def __init__(self, position, scale, color):
        super().__init__(position, scale, color)
    
    def draw(self):
        glPushMatrix()
        super().draw()
        glBegin(GL_POLYGON)
        glVertex2f(0, -0.5)
        glVertex2f(-0.5, 0)
        glVertex2f(-0.25, 0.5)
        glVertex2f(0, 0)
        glVertex2f(0.25, 0.5)
        glVertex2f(0.5, 0)
        glEnd()
        glPopMatrix()