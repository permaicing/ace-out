from math import pi as PI, sin, cos
from src.primitives.Primitive import Primitive
from OpenGL.GL import *

class Eneagon(Primitive):
    def __init__(self, position, scale, color, n_sides):
        super().__init__(position, scale, color)
        self.n_sides = n_sides
        self.depth = 1  # A profundidade que define a espessura do eneágono

    def draw(self):
        glPushMatrix()
        super().draw()

        # Desenhar a face da frente (z = depth / 2)
        glBegin(GL_POLYGON)
        for i in range(self.n_sides):
            theta = i * (2.0 * PI / self.n_sides)
            glVertex3f(cos(theta), sin(theta), self.depth / 2)
        glEnd()

        # Desenhar a face de trás (z = -depth / 2)
        glBegin(GL_POLYGON)
        for i in range(self.n_sides):
            theta = i * (2.0 * PI / self.n_sides)
            glVertex3f(cos(theta), sin(theta), -self.depth / 2)
        glEnd()

        # Desenhar as laterais
        glBegin(GL_QUAD_STRIP)
        for i in range(self.n_sides):
            theta = i * (2.0 * PI / self.n_sides)
            next_theta = (i + 1) * (2.0 * PI / self.n_sides)

            # Vértices da face da frente
            x1, y1 = cos(theta), sin(theta)
            x2, y2 = cos(next_theta), sin(next_theta)

            # Vértices da face de trás
            glVertex3f(x1, y1, self.depth / 2)    # Face da frente
            glVertex3f(x1, y1, -self.depth / 2)   # Face de trás
            glVertex3f(x2, y2, self.depth / 2)    # Face da frente
            glVertex3f(x2, y2, -self.depth / 2)   # Face de trás

        glEnd()

        glPopMatrix()
