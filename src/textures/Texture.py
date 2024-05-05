from OpenGL.GL import *
from PIL import Image

class Texture():

    texs = {}

    def __init__(self, filepath, wrapping = GL_CLAMP, filtering = GL_LINEAR):
        self.texId = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texId)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, wrapping)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, wrapping)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, filtering)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, filtering)
        image = Image.open(filepath).transpose(Image.FLIP_TOP_BOTTOM)
        imageData = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, imageData)
        glGenerateMipmap(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, 0)

    def useTexture(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texId)

    def destroyTexture(self):
        glDeleteTextures(1, self.texId)
