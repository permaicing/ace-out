from random import random, uniform
from math import sqrt
from src.primitives.Heart import Heart
from src.primitives.Shield import Shield
from src.objects.Ship import Ship
from src.objects.EnemyA import EnemyA
from src.objects.EnemyB import EnemyB
from src.objects.Background import Background
from src.textures.Texture import Texture
from OpenGL.GL import *
from OpenGL.GLUT import *
from glm import *
import glm
import math

class Game:
    def __init__(self):
        # Startup
        glClearColor(0, 0, 0, 1)
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_TEXTURE_2D)
        Texture.texs.update({
            # 'ship': Texture('src/textures/ships/player_ship.png'),
            'bullet': Texture('src/textures/bullets/bullet.png'),
            'scenario': Texture('src/textures/bgs/space.png', GL_REPEAT),
        })
        
        self.FPS = 60
        self.front = False
        self.back = False
        self.left = False
        self.right = False

        self.windowH = 360
        self.windowW = 640
        self.sceneH = 20
        self.sceneW = 20

        # Status
        self.HP = 3
        self.upgrades = 0
        
        # Objects
        self.ship = Ship("src/models/player/player_ship.obj", "src/models/player/player_ship.mtl")
        self.projectiles = []
        self.enemies = []
        self.background = Background(Texture.texs['scenario'].texId, self.sceneW)

        self.camPos = self.ship.position        
        self.lightPosition = glm.vec3(-20, -20, 5)  # Posição da fonte de luz
        self.lightAmbient = glm.vec3(0.1)       # Propriedade ambiente da fonte de luz
        self.lightDiffuse = glm.vec3(1.0)       # Propriedade difusa da fonte de luz
        self.lightSpecular = glm.vec3(1.0)      # Propriedade especular da fonte de luz                                              

        self.lightAngle = 0  # angulo inicial para movimento da luz

    def keyboardSpecial(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.left = True
        elif key == GLUT_KEY_RIGHT:
            self.right = True

    def keyboardSpecialUp(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.left = False
        elif key == GLUT_KEY_RIGHT:
            self.right = False

    def reshape(self, w, h):
        self.windowW = w
        self.windowH = h
        self.sceneW = self.sceneH * w / h

        self.background.width = self.sceneW
        glViewport(0, 0, w, h)

    def timer(self, v):
        glutTimerFunc(int(1000 / self.FPS), self.timer, 0)
        
        # Spawn enemies
        if random() < 0.005:
            if len(self.enemies) < 5:
                posX = uniform(-self.sceneW/2+1.15, self.sceneW/2-1.15)
                if random() < 0.45:
                    self.enemies.append(EnemyA(posX))
                else:
                    self.enemies.append(EnemyB(posX))
        
        # Update positions
        self.ship.updatePosition(self)

        for projectil in self.projectiles:
            projectil.updatePosition()
            if (projectil.position.y > self.sceneH/2) or (projectil.position.y < -self.sceneH/2):
                self.projectiles.remove(projectil)
        
        for enemy in self.enemies:
            enemy.updatePosition()
            if enemy.position.y < -7 or abs(enemy.position.x) > self.sceneW:
                self.enemies.remove(enemy)
        self.background.updatePosition()

        # Firing
        self.ship.fireGauge -= 1
        self.ship.fire(self)
        for enemy in self.enemies:
            enemy.fireGauge -= 1
            enemy.fire(self)
        
        # Collision detection
        for projectile in self.projectiles:
            if not projectile.isEnemy:
                for enemy in self.enemies:
                    d = distance(projectile.position, enemy.position)
                    if (d <= 1 and isinstance(enemy, EnemyA) or \
                        d <= 1.25 and isinstance(enemy, EnemyB)):
                        self.upgrades = min(self.upgrades+1, 3)
                        self.enemies.remove(enemy)
                        self.projectiles.remove(projectile)
                        break
            else:
                d = distance(projectile.position, self.ship.position)
                if d <= 0.5:
                    self.projectiles.remove(projectile)
                    if self.upgrades > 0:
                        self.upgrades -= 1
                    else:
                        self.HP -= 1
                        if self.HP == 0:
                            glutLeaveMainLoop()

        # Atualizar a posição da luz
        self.lightAngle += 0.01  # velocidade do movimento
        self.lightPosition.x = 10 * math.cos(self.lightAngle)
        self.lightPosition.y = 10 * math.sin(self.lightAngle)

        glutPostRedisplay()

    def drawHUD(self):
        # Salva a matriz de projeção atual
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()

        # Configura a projeção ortográfica para a HUD
        glOrtho(0, self.windowW, 0, self.windowH, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # Desenha a HUD
        for i in range(self.HP):
            Heart(
                vec3(15 + i * 30, self.windowH - 45, 0),
                vec3(25, 25, 1),
                (1, 0, 1)
            ).draw()

        for i in range(int(self.upgrades)):
            Shield(
                vec3(self.windowW - 45 - i * 30, self.windowH - 45, 0),
                vec3(25, 25, 1),
                (0, 1, 1)
            ).draw()

        # Restaura as matrizes anteriores
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def mat2list(self, M):
        matrix = []
        for i in range(0,4):
            matrix.append(list(M[i]))
        return matrix

    def run(self):
        # Habilitar o teste de profundidade
        glEnable(GL_DEPTH_TEST)
        
        # Habilitar o back-face culling
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glFrontFace(GL_CCW)

        # Definir o teste de profundidade para desenhar apenas se o novo valor for menor
        glDepthFunc(GL_LESS)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = self.windowW / self.windowH
        glFrustum(-aspect_ratio, aspect_ratio, -1, 1, 1, 100)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Ajuste na posição da câmera e direção
        camPos = self.ship.position + vec3(0, -3.5, 3)
        targetPos = self.ship.position + vec3(0, 10, 0)
        upDir = vec3(0, 1, 0)

        matrizCamera = lookAt(camPos, targetPos, upDir)
        glLoadMatrixf(self.mat2list(matrizCamera))

        # Desabilitar o culling temporariamente para desenhar o skybox
        glDisable(GL_CULL_FACE)
        self.background.draw()
        glEnable(GL_CULL_FACE)

        # Atualizações na nave
        self.ship.fireGaugeFull = 100 - self.upgrades * 5
        self.ship.velocity = (0.2 + 0.03 * self.upgrades) * vec3(1, 0, 0)

        # Desenhar projéteis, também sem culling
        glDisable(GL_CULL_FACE)
        for projectile in self.projectiles:
            projectile.draw()
        glEnable(GL_CULL_FACE)

        # Desenhar a nave
        self.ship.draw(self)

        # Desenhar inimigos
        for enemy in self.enemies:
            enemy.draw(self)

        # Desenhar a fonte de luz
        glColor3f(1, 1, 0)
        glPointSize(20)
        glBegin(GL_POINTS)
        glVertex3f(self.lightPosition.x, self.lightPosition.y, self.lightPosition.z)
        glEnd()

        glDisable(GL_CULL_FACE)
        # Desenha a HUD (em 2D, sem profundidade)
        glDisable(GL_DEPTH_TEST)
        self.drawHUD()
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        glutSwapBuffers()
