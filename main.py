from OpenGL.GLUT import *
from src.Game import Game

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow('Ace-Out')

    game = Game()
    glutInitWindowSize(game.janelaLar, game.janelaAlt)
    glutInitWindowPosition(0, 0)
    game.inicio()

    glutTimerFunc(int(1000 / game.FPS), game.timer, 0)
    glutSpecialFunc(game.tecladoSpecial)
    glutSpecialUpFunc(game.tecladoUpSpecial)
    glutReshapeFunc(game.reshape)
    glutDisplayFunc(game.run)
    glutMainLoop()