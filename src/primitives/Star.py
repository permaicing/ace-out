from math import pi as PI, sin, cos
from OpenGL.GL import *
from src.primitives.Primitive import Primitive

class Star(Primitive):
    def __init__(self, position, scale, color, n_corners):
        super().__init__(position, scale, color)
        self.n_corners = n_corners
        self.depth = 1  # A profundidade que define a espessura da estrela

    def draw(self):
        glPushMatrix()
        super().draw()

        theta = 0.0

        # Desenhar a face da frente da estrela (z = depth / 2)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.0, 0.0, self.depth / 2)  # Centro da estrela na frente
        for i in range(0, self.n_corners + 1):
            glVertex3f(cos(theta), sin(theta), self.depth / 2)
            theta += 2.0 * PI / self.n_corners
            glVertex3f(cos(theta) / 2.0, sin(theta) / 2.0, self.depth / 2)
            theta += 2.0 * PI / self.n_corners
        glEnd()

        # Desenhar a face de trás da estrela (z = -depth / 2)
        theta = 0.0
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.0, 0.0, -self.depth / 2)  # Centro da estrela atrás
        for i in range(0, self.n_corners + 1):
            glVertex3f(cos(theta), sin(theta), -self.depth / 2)
            theta += 2.0 * PI / self.n_corners
            glVertex3f(cos(theta) / 2.0, sin(theta) / 2.0, -self.depth / 2)
            theta += 2.0 * PI / self.n_corners
        glEnd()

        # Desenhar as laterais que conectam as faces da frente e de trás
        theta = 0.0
        glBegin(GL_QUAD_STRIP)
        for i in range(0, self.n_corners + 1):
            # Primeiro vértice da face da frente
            x1, y1 = cos(theta), sin(theta)
            # Primeiro vértice da face de trás
            x2, y2 = cos(theta) / 2.0, sin(theta) / 2.0
            # Conectar as bordas
            glVertex3f(x1, y1, self.depth / 2)    # Frente
            glVertex3f(x1, y1, -self.depth / 2)   # Trás

            theta += 2.0 * PI / self.n_corners
            glVertex3f(x2, y2, self.depth / 2)    # Frente
            glVertex3f(x2, y2, -self.depth / 2)   # Trás

            theta += 2.0 * PI / self.n_corners
        glEnd()

        glPopMatrix()
