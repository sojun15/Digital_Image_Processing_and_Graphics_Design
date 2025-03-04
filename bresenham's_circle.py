from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 500, 500

def midpoint_circle(radius):
    x = 0
    y = radius
    p = 3 - (2 * radius)

    glBegin(GL_POINTS) 

    while x <= y:
        draw_circle_points(x, y)
        if p < 0: 
            p = p + (4 * x) + 6
        else: 
            p = p + 4 * (x - y) + 10
            y -= 1 

        x += 1 

    glEnd()
    glFlush() 

def draw_circle_points(x, y):
    glVertex2i(x + 250, y + 250)  
    glVertex2i(-x + 250, y + 250) 
    glVertex2i(x + 250, -y + 250) 
    glVertex2i(-x + 250, -y + 250) 
    glVertex2i(y + 250, x + 250) 
    glVertex2i(-y + 250, x + 250)
    glVertex2i(y + 250, -x + 250) 
    glVertex2i(-y + 250, -x + 250)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Set circle color to white
    glColor3f(1.0, 1.0, 1.0)  
    glPointSize(1)
    midpoint_circle(50)
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    gluOrtho2D(0, width, 0, height) 

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Midpoint Circle Algorithm")
init()
glutDisplayFunc(display)
glutMainLoop()