from OpenGL.GL import *
import numpy as np
import glm
from OpenGL.arrays import vbo

class Mesh:
    def __init__(self, objFilepath, mtlFilepath):
        self.vertices = self.loadObjectFile(objFilepath)
        self.position = glm.vec3(0, 0, 0)
        self.scale = glm.vec3(1, 1, 1)
        self.rotation = glm.vec4(0, 0, 1, 0)
        # self.materials = {}
        # self.currentMaterial = None
        # self.loadMaterialsFile(mtlFilepath)
        self.vbo = vbo.VBO(np.array(self.vertices, dtype=np.float32))

    def readVertex(self, words):
        return [float(words[1]), float(words[2]), float(words[3])]

    def readTextcoord(self, words):
        return [float(words[1]), float(words[2])]

    def readNormal(self, words):
        return [float(words[1]), float(words[2]), float(words[3])]

    def readFace(self, words, v, vt, vn, vertices):
        numOfTriangles = len(words) - 3
        for i in range(numOfTriangles):
            self.createCorner(words[1], v, vt, vn, vertices)
            self.createCorner(words[i + 2], v, vt, vn, vertices)
            self.createCorner(words[i + 3], v, vt, vn, vertices)

    def createCorner(self, word, v, vt, vn, vertices):
        data = word.split('/')
        for element in v[int(data[0]) - 1]:
            vertices.append(element)
        for element in vt[int(data[1]) - 1]:
            vertices.append(element)
        for element in vn[int(data[2]) - 1]:
            vertices.append(element)

    def loadObjectFile(self, filename):
        v = []
        vt = []
        vn = []
        vertices = []
        with open(filename, "r") as file:
            line = file.readline()
            while line:
                words = line.split()
                match words[0]:
                    case "v":
                        v.append(self.readVertex(words))
                    case "vt":
                        vt.append(self.readTextcoord(words))
                    case "vn":
                        vn.append(self.readNormal(words))
                    case "f":
                        self.readFace(words, v, vt, vn, vertices)
                line = file.readline()

        return vertices
    
    """
   
    def readMaterial(self, words):
        return words[1]
    
    def readColor(self, words):
        return [float(words[1]), float(words[2]), float(words[3])]
    
    def readShininess(self, words):
        return float(words[1])

    def readIllum(self, words):
        return int(words[1])

    def loadMaterialsFile(self, filename):
        currentMaterial = None
        with open(filename, "r") as file:
            line = file.readline()
            while line:
                words = line.split()
                match words[0]:
                    case "newmtl":
                        currentMaterial = self.readMaterial(words)
                        self.materials[currentMaterial] = {}
                    case "Ns":
                        self.materials[currentMaterial]['shininess'] = self.readShininess(words)
                    case "Ka":
                        self.materials[currentMaterial]['ambient'] = self.readColor(words)
                    case "Kd":
                        self.materials[currentMaterial]['diffuse'] = self.readColor(words)
                    case "Ks":
                        self.materials[currentMaterial]['specular'] = self.readColor(words)
                    case "Ke":
                        self.materials[currentMaterial]['emissive'] = self.readColor(words)
                    case "Ni":
                        self.materials[currentMaterial]['optical_density'] = float(words[1])
                    case "d":
                        self.materials[currentMaterial]['dissolve'] = float(words[1])
                    case "illum":
                        self.materials[currentMaterial]['illumination_model'] = self.readIllum(words)
                        
    """

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glScalef(self.scale.x, self.scale.y, self.scale.z)
        glRotatef(self.rotation.w, self.rotation.x, self.rotation.y, self.rotation.z)

        #luz temporaria para debug
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        # for material, properties in self.materials.items():
        #     glMaterialfv(GL_FRONT, GL_AMBIENT, properties['ambient'])
        #     glMaterialfv(GL_FRONT, GL_DIFFUSE, properties['diffuse'])
        #     glMaterialfv(GL_FRONT, GL_SPECULAR, properties['specular'])
        #     glMaterialfv(GL_FRONT, GL_EMISSION, properties['emission'])
        #     glMaterialf(GL_FRONT, GL_SHININESS, properties['shininess'])

        self.vbo.bind()
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)

        glVertexPointer(3, GL_FLOAT, 32, self.vbo)
        glTexCoordPointer(2, GL_FLOAT, 32, self.vbo + 12)
        glNormalPointer(GL_FLOAT, 32, self.vbo + 20)
        glDrawArrays(GL_TRIANGLES, 0, len(self.vertices) // 8)

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        self.vbo.unbind()

        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)

        glPopMatrix()