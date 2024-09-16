from OpenGL.GL import *
from src.primitives.Primitive import Primitive

class Triangle(Primitive):
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
        self.color = color
        self.texture = texture
    
    def draw(self):
        glPushMatrix()
        super().draw()
        if self.texture: #Set the texture coordinates
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glBegin(GL_TRIANGLES)
            glColor3f(self.color[0], self.color[1], self.color[2])

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
            glColor3f(self.color[0], self.color[1], self.color[2])
            glVertex2f(-0.5, -0.5)
            glVertex2f(0, 0.5)
            glVertex2f(0.5, -0.5)
            glEnd()
        glPopMatrix()