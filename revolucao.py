from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import sys

ESCAPE = '\033'

def init():
   light_ambient =  [0.0, 0.0, 0.0, 1.0]
   light_diffuse =  [1.0, 1.0, 1.0, 1.0]
   light_specular =  [1.0, 1.0, 1.0, 1.0]
   light_position =  [1.0, 1.0, 1.0, 0.0]

   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
   glLightfv(GL_LIGHT0, GL_POSITION, light_position)

   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_DEPTH_TEST)


def display():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glRotatef(20.0, 1.0, 0.0, 0.0)

   glPushMatrix()
   glRotatef(180.0, 100.0, 0.0, 0.0)

   glPushMatrix()
   glTranslatef(-1.1, -0.75, 0.0)
   glutSolidSphere(1.0, 15, 15)
   glPopMatrix()

   glPopMatrix()
   glFlush()


def reshape(w, h):
   glViewport(0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()

   glOrtho(-2.5, 2.5, -2.5, 2.5, -10.0, 10.0)
   
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()

def keyPressed(tecla):
    if tecla == ESCAPE:
        glutLeaveMainLoop()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize (500, 500)
glutCreateWindow('revolucao')
init()
glutReshapeFunc(reshape)
glutKeyboardFunc(keyPressed)
glutDisplayFunc(display)
glutMainLoop()