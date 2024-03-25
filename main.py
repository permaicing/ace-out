from OpenGL.GL import *
from OpenGL.GLUT import *
from game import Game




if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(320, 640)
    glutCreateWindow('Ace-Out')
    glutDisplayFunc(Game.run)
    glClearColor(0, 0, 0, 1)
    glutMainLoop()