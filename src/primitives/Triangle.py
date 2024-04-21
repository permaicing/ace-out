from OpenGL.GL import *
from src.primitives.Primitive import Primitive

class Triangle(Primitive):
    def __init__(self, position, scale, color):
        super().__init__(position, scale, color)
    
    def draw(self):
        glPushMatrix()
        super().draw()
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.5, -0.5)
        glVertex2f(0, 0.5)
        glVertex2f(0.5, -0.5)
        glEnd()
        glPopMatrix()