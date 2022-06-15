from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def dda_dashed(sx, sy, ex, ey):
    glBegin(GL_POINTS)
    if sx != ex:
        m = (ey-sy)/(ex-sx)  # calculating the scope
    else:
        m = 2e18  # calculating the scope

    if m < 1 and m > -1:  # check if the line is steep
        while(sx != ex):
            if sx % 10 == 0:
                glVertex2f(sx, round(sy))
            sx = sx + 1
            sy = sy + m
    else:
        while(sy != ey):
            if sy % 10 == 0:
                glVertex2f(round(sx), sy)
            sy = sy + 1
            sx = sx + (1/m)
    glVertex2f(ex, ey)
    glEnd()


def dda(sx, sy, ex, ey):
    glBegin(GL_POINTS)
    if sx != ex:
        m = (ey-sy)/(ex-sx)  # calculating the scope
    else:
        m = 2e18  # calculating the scope

    if m < 1 and m > -1:  # check if the line is steep
        while(sx != ex):
            glVertex2f(sx, round(sy))
            sx = sx + 1
            sy = sy + m
    else:
        while(sy != ey):
            glVertex2f(round(sx), sy)
            sy = sy + 1
            sx = sx + (1/m)
    glVertex2f(ex, ey)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 0)
    glPointSize(5)
    dda(00, 00, 00, 00)
    dda_dashed(400, 300, 400, 700)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 750)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"task03 -18101478")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
