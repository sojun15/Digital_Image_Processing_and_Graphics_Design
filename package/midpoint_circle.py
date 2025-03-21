from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

class Mid_point:
    def __init__(self,count):
        # window size 
        width, height = 500, 500

        def midpoint_circle(cx, cy, radius):
            x = 0
            y = radius
            p = 1 - radius

            glBegin(GL_POINTS) 

            while x <= y:
                draw_circle_points(cx, cy, x, y)
                if p < 0: 
                    p = p + (2 * x) + 3
                else: 
                    p = p + 2 * (x - y) + 5
                    y -= 1 

                x += 1 

            glEnd()
            glFlush() 

        def draw_circle_points(cx, cy, x, y):
            glVertex2i(cx + x, cy + y)  
            glVertex2i(cx - x, cy + y) 
            glVertex2i(cx + x, cy - y) 
            glVertex2i(cx - x, cy - y) 
            glVertex2i(cx + y, cy + x) 
            glVertex2i(cx - y, cy + x)
            glVertex2i(cx + y, cy - x) 
            glVertex2i(cx - y, cy - x)

        def display():
            glClear(GL_COLOR_BUFFER_BIT)
            glColor3f(1.0, 1.0, 1.0)  # White color
            glPointSize(1)

            for x in range(count):
                cx = random.randint(50, width - 50)  # Random X position
                cy = random.randint(50, height - 50) # Random Y position
                radius = random.randint(10, 40)      # Random radius
                midpoint_circle(cx, cy, radius)

            glFlush()

        def init():
            glClearColor(0.0, 0.0, 0.0, 1.0) 
            gluOrtho2D(0, width, 0, height)  

        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(width, height)
        glutCreateWindow(b"50 Circles with OpenGL")
        init()
        glutDisplayFunc(display)
        glutMainLoop()