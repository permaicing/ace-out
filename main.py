from OpenGL.GLUT import *
from src.Game import Game

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow('Ace-Out')

    game = Game()
    glutInitWindowSize(game.windowW, game.windowH)
    glutInitWindowPosition(0, 0)

    glutTimerFunc(int(1000 / game.FPS), game.timer, 0)
    glutSpecialFunc(game.keyboardSpecial)
    glutSpecialUpFunc(game.keyboardSpecialUp)
    glutReshapeFunc(game.reshape)
    glutDisplayFunc(game.run)
    glutMainLoop()