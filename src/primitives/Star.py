from math import pi as PI, sin, cos
from OpenGL.GL import *
from src.primitives.Primitive import Primitive
import glm

class Star(Primitive):
    def __init__(self, position, scale, color, n_corners):
        super().__init__(
            position,
            scale,
            glm.vec3(0.1),
            glm.vec3(color[0], color[1], color[2]),
            glm.vec3(0.5),
            128
        )

        self.n_corners = n_corners
        self.depth = 1  # A profundidade que define a espessura da estrela

    def draw(self, game):
        glPushMatrix()
        
        # Aplicar a transformação (rotação, escalonamento, etc.)
        super().draw()

        theta = 0.0

        # Desenhar a face da frente da estrela (z = depth / 2)
        normal = glm.vec3(0, 0, 1)
        glBegin(GL_TRIANGLE_FAN)

        vertex = glm.vec3(0.0, 0.0, self.depth / 2)
        cor = super().shading(vertex, normal, game)
        glColor3f(cor.r, cor.g, cor.b)
        glVertex3f(vertex.x, vertex.y, vertex.z)

        for i in range(self.n_corners + 1):
            vertex = glm.vec3(cos(theta), sin(theta), self.depth / 2)
            cor = super().shading(vertex, normal, game)
            glColor3f(cor.r, cor.g, cor.b)
            glVertex3f(vertex.x, vertex.y, vertex.z)

            theta += 2.0 * PI / self.n_corners

            vertex = glm.vec3(cos(theta) / 2.0, sin(theta) / 2.0, self.depth / 2)
            cor = super().shading(vertex, normal, game)
            glColor3f(cor.r, cor.g, cor.b)
            glVertex3f(vertex.x, vertex.y, vertex.z)

            theta += 2.0 * PI / self.n_corners
        glEnd()

        # Desenhar a face de trás da estrela (z = -depth / 2)
        theta = 0.0
        normal = glm.vec3(0, 0, -1)  # Normal para a parte de trás
        glBegin(GL_TRIANGLE_FAN)

        vertex = glm.vec3(0.0, 0.0, -self.depth / 2)
        cor = super().shading(vertex, normal, game)
        glColor3f(cor.r, cor.g, cor.b)
        glVertex3f(vertex.x, vertex.y, vertex.z)

        for i in range(self.n_corners + 1):
            vertex = glm.vec3(cos(theta), sin(theta), -self.depth / 2)
            cor = super().shading(vertex, normal, game)
            glColor3f(cor.r, cor.g, cor.b)
            glVertex3f(vertex.x, vertex.y, vertex.z)

            theta += 2.0 * PI / self.n_corners

            vertex = glm.vec3(cos(theta) / 2.0, sin(theta) / 2.0, -self.depth / 2)
            cor = super().shading(vertex, normal, game)
            glColor3f(cor.r, cor.g, cor.b)
            glVertex3f(vertex.x, vertex.y, vertex.z)

            theta += 2.0 * PI / self.n_corners
        glEnd()

        # Desenhar as laterais que conectam as faces da frente e de trás
        theta = 0.0
        glBegin(GL_QUAD_STRIP)
        for i in range(self.n_corners + 1):
            # Primeiro vértice da face da frente
            x1, y1 = cos(theta), sin(theta)
            # Primeiro vértice da face de trás
            x2, y2 = cos(theta) / 2.0, sin(theta) / 2.0

            # Vértice da frente
            front_vertex = glm.vec3(x1, y1, self.depth / 2)
            front_normal = glm.normalize(glm.vec3(x1, y1, 0))
            front_color = super().shading(front_vertex, front_normal, game)
            glColor3f(front_color.r, front_color.g, front_color.b)
            glVertex3f(x1, y1, self.depth / 2)

            # Vértice de trás
            back_vertex = glm.vec3(x1, y1, -self.depth / 2)
            back_normal = glm.normalize(glm.vec3(x1, y1, 0))
            back_color = super().shading(back_vertex, back_normal, game)
            glColor3f(back_color.r, back_color.g, back_color.b)
            glVertex3f(x1, y1, -self.depth / 2)

            # Conectar as bordas
            glVertex3f(x2, y2, self.depth / 2)
            glVertex3f(x2, y2, -self.depth / 2)

            theta += 2.0 * PI / self.n_corners
        glEnd()

        glPopMatrix()
