from OpenGL.GL import *
from OpenGL.GLUT import *
from objects import Ship


class Game:

    def __init__(self):
        self.ship = Ship([0, -0.9], [0, 0, 1], 0.1, 0.05)

    # Handlers
    def keyboard(self, key, x, y):
        if key == b'\x1B':
            glutLeaveMainLoop()
        elif key == b'a':
            self.ship.move_left(self.ship.speed)
        elif key == b'w':
            self.ship.move_up(self.ship.speed)
        elif key == b's':
            self.ship.move_down(self.ship.speed)
        elif key == b'd':
            self.ship.move_right(self.ship.speed)

    def run(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        self.ship.draw()

        glutSwapBuffers()