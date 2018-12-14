#! /usr/bin/env python
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import sys
import png

ESCAPE = '\033'

def LoadTextures():
	global texture

	################################################################################
	index = 0
	texture = glGenTextures(2)
	files = ('sorvete.png', 'casquinha.png')

	for file in files:
		glBindTexture(GL_TEXTURE_2D, texture[index])
		reader = png.Reader(filename=file)
		w, h, pixels, metadata = reader.read_flat()
		
		if(metadata['alpha']):
		    modo = GL_RGBA
		else:
		    modo = GL_RGB

		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		index = index + 1
	################################################################################

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
   #glPushMatrix()
   glRotatef(20.0, 1.0, 0.0, 0.0)

   glPushMatrix()
   glRotatef(180.0, 100.0, 0.0, 0.0)

   # CARREGA TEXTURAS
   glEnable( GL_TEXTURE_2D );
   glEnable(GL_TEXTURE_GEN_S);
   glEnable(GL_TEXTURE_GEN_T);
   glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR);
   glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP);

   # DESENHA CASQUINHA
   glPushMatrix()
   glBindTexture(GL_TEXTURE_2D, texture[1])
   glTranslatef(-1.1, -0.5, 0.0);
   glRotatef (270.0, 1.0, 0.0, 0.0)
   glutSolidCone(1.0, 2.0, 17, 18)
   glPopMatrix()

   # DESENHA SORVETE
   glPushMatrix()
   glTranslatef(-1.1, -0.75, 0.0)
   glBindTexture(GL_TEXTURE_2D, texture[0])
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
glutCreateWindow('sorvete')
LoadTextures()
init()
glutReshapeFunc(reshape)
glutKeyboardFunc(keyPressed)
glutDisplayFunc(display)
glutMainLoop()