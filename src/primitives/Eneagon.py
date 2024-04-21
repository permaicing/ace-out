from math import pi as PI, sin, cos
from src.primitives.Primitive import Primitive
from OpenGL.GL import *

class Eneagon(Primitive):
    def __init__(self, position, scale, color, n_sides):
        super().__init__(position, scale, color)
        self.n_sides = n_sides
    
    def draw(self):
        glPushMatrix()
        super().draw()
        glBegin(GL_POLYGON)        
        for i in range(0, self.n_sides):
            theta = i * (2.0*PI/self.n_sides)
            glVertex2f(cos(theta), sin(theta))
        glEnd()
        glPopMatrix()