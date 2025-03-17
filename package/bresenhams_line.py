from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd

class Bresenhams:
    def __init__(self,count):
        # Window size
        width, height = 800, 600

        def bresenham_line(x1, y1, x2, y2):
            glBegin(GL_POINTS)  

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            m = dy / dx 
            if(dy<dx):
                p = 2 * dy - dx
            else:
                p = 2 * dx - dy

            if m < 1:
                while x1 != x2 or y1 != y2:
                    glVertex2i(x1, y1)
                    if p < 0:
                        xi1 = x1 + 1
                        yi1 = y1
                        pk1 = p + 2 * dy
                    else:
                        xi1 = x1 + 1
                        yi1 = y1 + 1
                        pk1 = p + 2 * (dy - dx)
                    x1, y1, p = xi1, yi1, pk1

            else:
                while x1 != x2 or y1 != y2:
                    glVertex2i(x1, y1)
                    if p < 0:
                        xi1 = x1
                        yi1 = y1 + 1
                        pk1 = p + 2 * dx
                    else:
                        xi1 = x1 + 1
                        yi1 = y1 + 1
                        pk1 = p + 2 * (dx - dy)
                    x1, y1, p = xi1, yi1, pk1

            glEnd()  
            glFlush()  

        # OpenGL Display Function
        def display():
            glClear(GL_COLOR_BUFFER_BIT)
            glColor3f(1, 0.3, 0.5)  # Set line color to white
            glPointSize(2)  # Pixel size
            for x in range(count):
                bresenham_line(rd.randint(30,60), rd.randint(30,60), rd.randint(300,500), rd.randint(300,500))
            glFlush()

        # OpenGL Initialization
        def init():
            glClearColor(0.0, 0.0, 0.0,0.0)  # Set background color to black
            gluOrtho2D(0, width, 0, height)  # Set coordinate system

        # Main Function
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(b"Bresenham's Line Algorithm")
        init()
        glutDisplayFunc(display)
        glutMainLoop()

