from OpenGL.GL import *
from OpenGL.GLUT import *
from game import Game


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(640, 640)
    glutCreateWindow('Ace-Out')
    glClearColor(0, 0, 0, 1)
    
    game = Game()

    glutKeyboardFunc(game.keyboard)
    glutDisplayFunc(game.run)
    glutIdleFunc(game.run)
    
    glutMainLoop()