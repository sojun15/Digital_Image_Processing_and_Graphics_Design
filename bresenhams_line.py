from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

# Bresenham's Line Drawing Algorithm
def bresenham_line(x1, y1, x2, y2):
    glBegin(GL_POINTS)  # Start drawing pixels

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
    glColor3f(1.0, 1.0, 1.0)  # Set line color to white
    glPointSize(2)  # Pixel size
    bresenham_line(50, 50, 400, 300)  # Draw line from (50,50) to (400,300)
    glFlush()

# OpenGL Initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
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
