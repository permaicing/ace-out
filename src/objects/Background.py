from OpenGL.GL import *

class Background:
    def __init__(self, texture, size):
        self.texture = texture
        self.size = size * 3
        
        self.position = 0.0
        self.speed = 0.001

    def updatePosition(self):
        self.position += self.speed
        if self.position > 1.0:
            self.position -= 1.0

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)

        glBegin(GL_QUADS)

        # Face dianteira (movimento de textura para trás)
        glTexCoord2f(self.position, 0.0)
        glVertex3f(-self.size, -self.size, self.size)
        glTexCoord2f(self.position, 1.0)
        glVertex3f(self.size, -self.size, self.size)
        glTexCoord2f(1.0 + self.position, 1.0)
        glVertex3f(self.size, self.size, self.size)
        glTexCoord2f(1.0 + self.position, 0.0)
        glVertex3f(-self.size, self.size, self.size)

        # Face traseira (movimento de textura para trás)
        glTexCoord2f(self.position, 0.0)
        glVertex3f(-self.size, -self.size, -self.size)
        glTexCoord2f(self.position, 1.0)
        glVertex3f(self.size, -self.size, -self.size)
        glTexCoord2f(1.0 + self.position, 1.0)
        glVertex3f(self.size, self.size, -self.size)
        glTexCoord2f(1.0 + self.position, 0.0)
        glVertex3f(-self.size, self.size, -self.size)

        # Face esquerda (movimento de textura para trás)
        glTexCoord2f(self.position, 0.0)
        glVertex3f(-self.size, -self.size, -self.size)
        glTexCoord2f(self.position, 1.0)
        glVertex3f(-self.size, -self.size, self.size)
        glTexCoord2f(1.0 + self.position, 1.0)
        glVertex3f(-self.size, self.size, self.size)
        glTexCoord2f(1.0 + self.position, 0.0)
        glVertex3f(-self.size, self.size, -self.size)

        # Face direita (movimento de textura para trás)
        glTexCoord2f(self.position, 0.0)
        glVertex3f(self.size, -self.size, -self.size)
        glTexCoord2f(self.position, 1.0)
        glVertex3f(self.size, -self.size, self.size)
        glTexCoord2f(1.0 + self.position, 1.0)
        glVertex3f(self.size, self.size, self.size)
        glTexCoord2f(1.0 + self.position, 0.0)
        glVertex3f(self.size, self.size, -self.size)

        # Face superior (movimento de textura do centro para fora)
        glTexCoord2f(0.5 - self.position, 0.5 - self.position)
        glVertex3f(-self.size, self.size, -self.size)
        glTexCoord2f(0.5 + self.position, 0.5 - self.position)
        glVertex3f(self.size, self.size, -self.size)
        glTexCoord2f(0.5 + self.position, 0.5 + self.position)
        glVertex3f(self.size, self.size, self.size)
        glTexCoord2f(0.5 - self.position, 0.5 + self.position)
        glVertex3f(-self.size, self.size, self.size)

        # Face inferior (movimento de textura para trás)
        glTexCoord2f(self.position, 0.0)
        glVertex3f(-self.size, -self.size, -self.size)
        glTexCoord2f(self.position, 1.0)
        glVertex3f(self.size, -self.size, -self.size)
        glTexCoord2f(1.0 + self.position, 1.0)
        glVertex3f(self.size, -self.size, self.size)
        glTexCoord2f(1.0 + self.position, 0.0)
        glVertex3f(-self.size, -self.size, self.size)

        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)
