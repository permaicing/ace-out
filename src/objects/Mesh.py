from OpenGL.GL import *
import numpy as np
import glm

class Mesh:
    def __init__(self, objFilepath, mtlFilepath, shading_frequency=10, ambient=None, diffuse=None, specular=None, shine=32.0):
        self.vertices = self.loadObjectFile(objFilepath)
        self.position = glm.vec3(0, 0, 0)
        self.scale = glm.vec3(1, 1, 1)
        self.rotation = glm.vec4(0, 0, 1, 0)

        # Definições de materiais (agora podem ser passadas como parâmetros)
        self.objectAmbient = ambient if ambient else glm.vec3(0.2, 0.2, 0.2)
        self.objectDiffuse = diffuse if diffuse else glm.vec3(0.8, 0.8, 0.8)
        self.objectSpecular = specular if specular else glm.vec3(1.0, 1.0, 1.0)
        self.objectShine = shine

        # Cores e renderização
        self.colors = []  # Lista para armazenar as cores calculadas
        self.shading_frequency = shading_frequency
        self.render_count = 0  # Contador de renderizações

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
            for line in file:
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

        return vertices

    def shading(self, point, normal, game):
        shadeAmbient = game.lightAmbient * self.objectAmbient

        l = glm.normalize(game.lightPosition - point)
        n = glm.normalize(normal)
        shadeDiffuse = game.lightDiffuse * self.objectDiffuse * glm.max(0.0, glm.dot(l, n))

        v = glm.normalize(game.camPos - point)
        r = 2 * glm.dot(n, l) * n - l
        shadeSpecular = game.lightSpecular * self.objectSpecular * glm.max(0, glm.dot(v, r) ** self.objectShine)

        shade = shadeAmbient + shadeDiffuse + shadeSpecular
        return shade

    def draw(self, game):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glScalef(self.scale.x, self.scale.y, self.scale.z)
        glRotatef(self.rotation.w, self.rotation.x, self.rotation.y, self.rotation.z)

        vertices = []  # Reinicializa a lista de vértices
        if self.render_count % self.shading_frequency == 0:
            self.colors.clear()  # Limpa a lista de cores antes de recalcular
            for i in range(0, len(self.vertices), 8):
                vertex = glm.vec3(self.vertices[i], self.vertices[i + 1], self.vertices[i + 2])
                normal = glm.vec3(self.vertices[i + 5], self.vertices[i + 6], self.vertices[i + 7])
                
                # Atualizando a posição do vértice
                vertices.extend([vertex.x, vertex.y, vertex.z])
                
                # Recalcular a cor se for o momento de recalcular
                color = self.shading(vertex, normal, game)
                self.colors.extend([color.r, color.g, color.b])
        else:
            # Reutilizando cores previamente calculadas, mas atualizando os vértices
            for i in range(0, len(self.vertices), 8):
                vertex = glm.vec3(self.vertices[i], self.vertices[i + 1], self.vertices[i + 2])
                vertices.extend([vertex.x, vertex.y, vertex.z])

        # Convertendo listas para arrays numpy
        vertices_array = np.array(vertices, dtype=np.float32)
        colors_array = np.array(self.colors, dtype=np.float32)

        # Desenho
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glVertexPointer(3, GL_FLOAT, 0, vertices_array)
        glColorPointer(3, GL_FLOAT, 0, colors_array)

        glDrawArrays(GL_TRIANGLES, 0, len(vertices) // 3)

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

        glPopMatrix()

        self.render_count += 1  # Incrementa o contador de renderizações