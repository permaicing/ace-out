from OpenGL.GL import *
from src.primitives.Primitive import Primitive

class Triangle(Primitive):
    def __init__(self, position, scale, color, texture = None):
        super().__init__(position, scale, color)
        self.texture = texture
    
    def draw(self):
        glPushMatrix()
        super().draw()
        if self.texture: #Set the texture coordinates
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glBegin(GL_TRIANGLES)
            glTexCoord2f(0.0, 0.0)
            glVertex2f(-0.5, -0.5)
            glTexCoord2f(0.5, 1.0)
            glVertex2f(0, 0.5)
            glTexCoord2f(1.0, 0.0)
            glVertex2f(0.5, -0.5)
            glEnd()
            glBindTexture(GL_TEXTURE_2D, 0)
        else:
            glBegin(GL_TRIANGLES)
            glVertex2f(-0.5, -0.5)
            glVertex2f(0, 0.5)
            glVertex2f(0.5, -0.5)
            glEnd()
        glPopMatrix()