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

        glColor3f(1.0, 1.0, 1.0)

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


        # Face superior (textura estática)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-self.size, self.size, -self.size)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(self.size, self.size, -self.size)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(self.size, self.size, self.size)
        glTexCoord2f(0.0, 1.0)
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
