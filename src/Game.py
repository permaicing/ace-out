from random import random, uniform
from math import sqrt
from src.objects.Ship import Ship
from src.primitive.Heart import Heart
from src.primitive.Shield import Shield
from src.objects.EnemyA import EnemyA
from src.objects.EnemyB import EnemyB
from OpenGL.GL import *
from OpenGL.GLUT import *
from glm import vec3

class Game:
    def __init__(self):
        self.ship = Ship()
        self.HP = 3
        self.upgrades = 10
        self.projectiles = []
        self.enemies = []

        self.FPS = 60
        self.frente = False
        self.tras = False
        self.esquerda = False
        self.direita = False

        self.janelaAlt = 80
        self.janelaLar = 80
        self.mundoAlt = 20
        self.muldoLar = 20

    def inicio(self):
        glClearColor(0, 0, 0, 1)
        glEnable(GL_MULTISAMPLE)

    def tecladoSpecial(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.esquerda = True
        elif key == GLUT_KEY_RIGHT:
            self.direita = True

    def tecladoUpSpecial(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.esquerda = False
        elif key == GLUT_KEY_RIGHT:
            self.direita = False

    def reshape(self, w, h):
        self.janelaLar = w
        self.janelaAlt = h
        self.mundoLar = self.mundoAlt * w / h
        glViewport(0, 0, w, h)

    def timer(self, v):
        glutTimerFunc(int(1000 / self.FPS), self.timer, 0)
        
        # Spawn enemies
        if random() < 0.005:
            posX = uniform(-self.mundoLar/2+1.15, self.mundoLar/2-1.15)
            if random() < 0.5:
                self.enemies.append(EnemyA(posX))
            else:
                self.enemies.append(EnemyB(posX))
        
        # Update positions
        self.ship.updatePosition(self)

        for projectil in self.projectiles:
            projectil.updatePosition()
            if (projectil.position.y > self.mundoAlt/2) or (projectil.position.y < -self.mundoAlt/2):
                self.projectiles.remove(projectil)
        
        for enemy in self.enemies:
            enemy.updatePosition()
            if enemy.position.y < -self.mundoAlt/2-2:
                self.enemies.remove(enemy)
        
        # Firing
        self.ship.fireRate -= 1
        self.ship.atirar(self)
        for enemy in self.enemies:
            enemy.fireRate -= 1
            enemy.atirar(self)
        
        glutPostRedisplay()

    def run(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.mundoLar / 2, self.mundoLar / 2, -self.mundoAlt / 2, self.mundoAlt / 2, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Drawings

        for i in range(self.HP):
            Heart(
                vec3(-self.mundoLar/2+1.15+i*0.6, self.mundoAlt/2-1.15, 1),
                vec3(0.5, 0.5, 1),
                (1, 0, 1)
            ).draw()
        for i in range(self.upgrades):
            Shield(
                vec3(self.mundoLar/2-1.15-i*0.6, self.mundoAlt/2-1.15, 1),
                vec3(0.5, 0.5, 1),
                (0, 1, 1)
            ).draw()

        for projectile in self.projectiles:
            projectile.draw()

        self.ship.draw()
        for enemy in self.enemies:
            enemy.draw()
        
        glutSwapBuffers()