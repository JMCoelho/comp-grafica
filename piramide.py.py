from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, pi
import sys

ESCAPE = '\033'
colors = ( 
        (1,0,0),
        (1,1,0),
        (0,1,0),
        (0,1,1),
        (0,0,1),
        (1,0,1),
        (0.5,1,1),
        (1,0,0.5) )
lados = 3

def desenhaPiramede(lados, r):
    teta = 0
    x = r
    y, z = 0, 0

    glBegin(GL_TRIANGLE_FAN)

    glColor3fv(colors[0])
    glVertex3f(0, r, 0)

    for v in range(lados+1):
        glColor3fv(colors[v%8])
        x2 = (x * cos(teta) - y * sin(teta))
        y2 = (x * sin(teta) + y * cos(teta))
        glVertex3f(x2, z, y2)
        teta += (2*pi)/lados
    glEnd()

    glBegin(GL_POLYGON)
    teta = 0
    for v in range(lados+1):
        glColor3fv(colors[v%8])
        x2 = (x * cos(teta) - y * sin(teta))
        y2 = (x * sin(teta) + y * cos(teta))
        glVertex3f(x2, z, y2)
        teta += (2*pi)/lados
    glEnd()

    #Linhas
    glBegin(GL_LINE_LOOP)
    teta = 0
    for v in range(lados+1):
        glColor3f(0,0,0)
        x2 = (x * cos(teta) - y * sin(teta))
        y2 = (x * sin(teta) + y * cos(teta))
        glVertex3f(x2, z, y2)
        teta += (2*pi)/lados
    glEnd()

    glBegin(GL_LINES)

    glColor3fv(colors[0])
    glVertex3f(0, r, 0)

    for v in range(lados+1):
        glColor3f(0,0,0)
        x2 = (x * cos(teta) - y * sin(teta))
        y2 = (x * sin(teta) + y * cos(teta))
        glVertex3f(0, r, 0)
        glVertex3f(x2, z, y2)
        teta += (2*pi)/lados
    glEnd()
    

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    desenhaPiramede(lados, 2)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def keyPressed(*args):
    global lados

    if args[0] == ESCAPE:
        glutLeaveMainLoop()
    else:
        nlados = int(args[0])
        if nlados >= 3:
            lados = nlados  

###########################################################################################
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide de N lados")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutKeyboardFunc(keyPressed)
glutMainLoop()