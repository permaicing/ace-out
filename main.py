from OpenGL.GLUT import *
from OpenGL.GL import *
from src.Game import Game
from src.textures.Texture import Texture

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow('Ace-Out')

    game = Game()
    glutInitWindowSize(game.windowW, game.windowH)
    glutInitWindowPosition(0, 0)
    glutReshapeWindow(game.windowW, game.windowH)

    glutTimerFunc(int(1000 / game.FPS), game.timer, 0)
    glutSpecialFunc(game.keyboardSpecial)
    glutSpecialUpFunc(game.keyboardSpecialUp)
    glutReshapeFunc(game.reshape)
    glutDisplayFunc(game.run)
    glutMainLoop()

    for tex in Texture.texs:
        tex.destroyTexture()