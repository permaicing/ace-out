from OpenGL.GL import *


class Background:

    def __init__(self, texture, width, height):
        self.texture = texture
        self.width = width
        self.height = height
        
        self.position = 0.0
        self.speed = 0.001

    def updatePosition(self):
        self.position += self.speed
        if self.position > 1.0:
            self.position = 0.0

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, self.position)
        glVertex2f(-self.width/2, -self.height/2)
        glTexCoord2f(1.0, self.position)
        glVertex2f(self.width/2, -self.height/2)
        glTexCoord2f(1.0, 1.0+self.position)
        glVertex2f(self.width/2, self.height/2)
        glTexCoord2f(0.0, 1.0+self.position)
        glVertex2f(-self.width/2, self.height/2)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)