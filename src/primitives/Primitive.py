from OpenGL.GL import *
import glm

class Primitive:
    def __init__(self, position, scale, objectAmbient, 
                    objectDiffuse, objectSpecular, 
                    objectShine, rotation = None):

        self.position = position
        self.scale = scale
        self.rotation = glm.vec4(0, 0, 1, 0) if rotation is None else rotation
        
        # Propriedades do material do objeto
        self.objectAmbient = objectAmbient
        self.objectDiffuse = objectDiffuse
        self.objectSpecular = objectSpecular
        self.objectShine = objectShine


    # Calcula a cor de sombreamento de um ponto usando o Modelo de IluminaÃ§Ã£o de Phong
    def shading(self, point, normal, game):
        # reflexÃ£o ambiente
        shadeAmbient = game.lightAmbient * self.objectAmbient

        # reflexÃ£o difusa
        l = glm.normalize(game.lightPosition - point)
        n = glm.normalize(normal)
        shadeDiffuse = game.lightDiffuse * self.objectDiffuse * glm.max(0.0, glm.dot(l,n))

        # reflexÃ£o especular
        v = glm.normalize(game.camPos - point)
        r = 2*glm.dot(n,l)*n - l
        shadeSpecular = game.lightSpecular * self.objectSpecular * glm.max(0, glm.dot(v,r) ** self.objectShine)

        # modelo de iluminaÃ§Ã£o de Phong
        shade = shadeAmbient + shadeDiffuse + shadeSpecular
        return shade
    
    """
    This function **MUST** be called inside a `glPushMatrix`/`glPopMatrix` pair.
    """
    def draw(self):
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glScalef(self.scale.x, self.scale.y, self.scale.z)
        glRotatef(self.rotation.w, self.rotation.x, self.rotation.y, self.rotation.z)