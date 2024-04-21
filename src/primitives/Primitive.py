from OpenGL.GL import *
import glm

class Primitive:
    def __init__(self, position, scale, color, rotation = None):
        self.position = position
        self.scale = scale
        self.rotation = glm.vec4(0, 0, 1, 0) if rotation is None else rotation
        self.color = color
    
    """
    This function **MUST** be called inside a `glPushMatrix`/`glPopMatrix` pair.
    """
    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glScalef(self.scale.x, self.scale.y, self.scale.z)
        glRotatef(self.rotation.w, self.rotation.x, self.rotation.y, self.rotation.z)