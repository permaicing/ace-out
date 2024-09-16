from OpenGL.GL import *
from src.primitives.Primitive import Primitive

class Rectangle(Primitive):
    def __init__(self, position, scale, color, objectAmbient, 
                    objectDiffuse, objectSpecular, 
                    objectShine, texture = None):

        super().__init__(            
            position,
            scale,
            objectAmbient,
            objectDiffuse,
            objectSpecular,
            objectShine
        )
        self.texture = texture
    
    def draw(self):
        glPushMatrix()
        super().draw()
        if self.texture: #Set the texture coordinates
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glTexCoord2f(0, 0)
            glVertex2f(-0.5, -0.5)
            glTexCoord2f(1, 0)
            glVertex2f(0.5, -0.5)
            glTexCoord2f(1, 1)
            glVertex2f(0.5, 0.5)
            glTexCoord2f(0, 1)
            glVertex2f(-0.5, 0.5)
            glEnd()
            glBindTexture(GL_TEXTURE_2D, 0)
        else:
            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex2f(-0.5, -0.5)
            glVertex2f(0.5, -0.5)
            glVertex2f(0.5, 0.5)
            glVertex2f(-0.5, 0.5)
            glEnd()
        glPopMatrix()