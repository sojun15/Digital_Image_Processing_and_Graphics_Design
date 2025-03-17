from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd

class Dda_line:
        def __init__(self,count):
            # Window size
            width, height = 600, 600

            def dda_line(x1, y1, x2, y2):
                dx = x2 - x1
                dy = y2 - y1
                steps = max(abs(dx), abs(dy)) 
                x_inc = dx / steps  
                y_inc = dy / steps  

                x, y = x1, y1 

                glBegin(GL_POINTS)  
                for x in range(int(steps) + 1):
                    glVertex2i(int(x), int(y)) 
                    x += x_inc
                    y += y_inc
                glEnd()
                glFlush() 

            def display():
                glClear(GL_COLOR_BUFFER_BIT) 
                glColor3f(1.0, 0.0, 0.0)  
                glPointSize(2) 
                for x in range(count):
                    dda_line(rd.randint(50,100), rd.randint(50,100), rd.randint(300,500), rd.randint(300,500))
                glFlush()

            def init():
                glClearColor(1.0, 1.0, 1.0, 1.0)  # Background color: black
                gluOrtho2D(0, width, 0, height)  # Set 2D coordinate system

            # Main Function
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
            glutInitWindowSize(width, height)
            glutInitWindowPosition(100, 100)
            glutCreateWindow(b"DDA Line Algorithm")
            init()
            glutDisplayFunc(display)
            glutMainLoop()
