from OpenGL.GL import *


class Object:

    def __init__(self, coords, color):
        self.coords = coords
        self.color = color
        self.vertices = []

    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        glBegin(GL_TRIANGLES)
        for vertex in self.vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

class Triangle(Object):

    def __init__(self, coords, color, length):
        super().__init__(coords, color)
        self.vertices = [
            [self.coords[0]-length/2, self.coords[1]-length/2],
            [self.coords[0]+length/2, self.coords[1]-length/2],
            [self.coords[0], self.coords[1]+length/2],
        ]
        self.length = length