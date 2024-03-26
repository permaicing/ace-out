from OpenGL.GL import *


class Object:

    def __init__(self, coords, color):
        self.coords = coords
        self.color = color
    
    def vertices(self):
        return []

    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        glBegin(GL_TRIANGLES)
        for vertex in self.vertices():
            glVertex2f(vertex[0], vertex[1])
        glEnd()

class Triangle(Object):

    def __init__(self, coords, color, length):
        super().__init__(coords, color)
        self.length = length
    
    def vertices(self):
        return [
            [self.coords[0]-self.length/2, self.coords[1]-self.length/2],
            [self.coords[0]+self.length/2, self.coords[1]-self.length/2],
            [self.coords[0], self.coords[1]+self.length/2],
        ]

class Diamond(Object):

    def __init__(self, coords, color, width, length):
        super().__init__(coords, color)
        self.width = width
        self.length = length
    
    def vertices(self):
        return [
            [self.coords[0]-self.width/2, self.coords[1]],
            [self.coords[0]+self.width/2, self.coords[1]],
            [self.coords[0], self.coords[1]+self.length/2],
            [self.coords[0], self.coords[1]-self.length/2],
        ]
    
    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        glBegin(GL_POLYGON)
        for vertex in self.vertices():
            glVertex2f(vertex[0], vertex[1])
        glEnd()