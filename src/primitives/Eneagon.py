from math import pi as PI, sin, cos
from OpenGL.GL import *
from src.primitives.Primitive import Primitive
import glm

class Eneagon(Primitive):
    def __init__(self, position, scale, color, n_sides):
        super().__init__(
            position,
            scale,
            glm.vec3(0.1),
            glm.vec3(color[0], color[1], color[2]),
            glm.vec3(0.5),
            128
        )
        self.n_sides = n_sides
        self.depth = 1  # A profundidade que define a espessura do eneágono

    def draw(self, game):
        glPushMatrix()
        super().draw()

        # Desenhar a face da frente (z = depth / 2)
        glBegin(GL_POLYGON)
        normal = glm.vec3(0, 0, 1)  # Normal para a face da frente
        for i in range(self.n_sides):
            theta = i * (2.0 * PI / self.n_sides)
            vertex = glm.vec3(cos(theta), sin(theta), self.depth / 2)
            color = super().shading(vertex, normal, game)
            glColor3f(color.r, color.g, color.b)
            glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()

        # Desenhar a face de trás (z = -depth / 2)
        glBegin(GL_POLYGON)
        normal = glm.vec3(0, 0, -1)  # Normal para a face de trás
        for i in range(self.n_sides):
            theta = i * (2.0 * PI / self.n_sides)
            vertex = glm.vec3(cos(theta), sin(theta), -self.depth / 2)
            color = super().shading(vertex, normal, game)
            glColor3f(color.r, color.g, color.b)
            glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()

        # Desenhar as laterais
        glBegin(GL_QUAD_STRIP)
        for i in range(self.n_sides):
            theta = i * (2.0 * PI / self.n_sides)
            next_theta = (i + 1) * (2.0 * PI / self.n_sides)

            # Vértices da face da frente
            x1, y1 = cos(theta), sin(theta)
            x2, y2 = cos(next_theta), sin(next_theta)

            # Vértices da face da frente
            front_vertex = glm.vec3(x1, y1, self.depth / 2)
            front_normal = glm.normalize(glm.vec3(x1, y1, 0))  # Normal na direção global
            front_color = super().shading(front_vertex, front_normal, game)
            glColor3f(front_color.r, front_color.g, front_color.b)
            glVertex3f(x1, y1, self.depth / 2)

            # Vértices da face de trás
            back_vertex = glm.vec3(x1, y1, -self.depth / 2)
            back_normal = glm.normalize(glm.vec3(x1, y1, 0))  # Normal na direção global
            back_color = super().shading(back_vertex, back_normal, game)
            glColor3f(back_color.r, back_color.g, back_color.b)
            glVertex3f(x1, y1, -self.depth / 2)

            # Conectar as bordas
            glVertex3f(x2, y2, self.depth / 2)
            glVertex3f(x2, y2, -self.depth / 2)

        glEnd()

        glPopMatrix()
