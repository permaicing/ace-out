from OpenGL.GL import *
from src.primitives.Primitive import Primitive

class Shield(Primitive):
    def __init__(self, position, scale, color):
        super().__init__(position, scale, None, None, None, None)

        self.color = color
    
    def draw(self):
        glPushMatrix()
        super().draw()
        glBegin(GL_POLYGON)
        glColor3f(self.color[0], self.color[1], self.color[2])
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