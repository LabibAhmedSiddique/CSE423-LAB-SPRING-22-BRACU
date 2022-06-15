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


def identify_zone(sx, sy, ex, ey):
    dx = ex - sx
    dy = ey - sy
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 'zone 0'
        elif dx < 0 and dy > 0:
            return'zone 3'
        elif dx < 0 and dy < 0:
            return'zone 4'
        elif dx > 0 and dy < 0:
            return'zone 7'
    else:
        if dx >= 0 and dy >= 0:
            return'zone 1'
        elif dx < 0 and dy > 0:
            return'zone 2'
        elif dx < 0 and dy < 0:
            return'zone 5'
        elif dx > 0 and dy < 0:
            return'zone 6'


def ctz0(x, y, sz):
    if sz == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif sz == 'zone 2':
        rx = y
        ry = (-1) * x
        return (rx, ry)
    elif sz == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif sz == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif sz == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif sz == 'zone 6':
        rx = (-1)*y
        ry = x
        return (rx, ry)
    elif sz == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


def cto(x, y, dz):
    if dz == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif dz == 'zone 2':
        rx = (-1) * y
        ry = x
        return (rx, ry)
    elif dz == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif dz == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif dz == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif dz == 'zone 6':
        rx = y
        ry = (-1)*x
        return (rx, ry)
    elif dz == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


def midpointLine(sx, sy, ex, ey):
    dy = ey-sy
    dx = ex-sx

    d_init = (2*dy) - dx
    d = d_init

    points = []
    if sx == ex:
        while(sy != ey):
            points.append((sx, sy))
            sy += 1
    elif sy == ey:
        while(sx != ex):
            points.append((sx, sy))
            sx += 1
    else:
        while(sx != ex and sy != ey):
            points.append((sx, sy))
            if d > 0:
                sx += 1
                sy += 1
                d += 2*(dy - dx)
            else:
                sx += 1
                d += 2*dy
    points.append((ex, ey))
    return points


def draw(sx, sy, ex, ey):
    glBegin(GL_POINTS)
    zone = identify_zone(sx, sy, ex, ey)

    if zone == 'zone 0':
        points = midpointLine(sx, sy, ex, ey)
        for point in points:
            glVertex2f(point[0], point[1])
    else:
        startingPointsConverted = ctz0(sx, sy, zone)
        endingPointConverted = ctz0(ex, ey, zone)
        points = midpointLine(
            startingPointsConverted[0], startingPointsConverted[1], endingPointConverted[0], endingPointConverted[1])
        for (x, y) in points:
            original = cto(x, y, zone)
            glVertex2f(original[0], original[1])
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 1, 0)
    glPointSize(5)

    draw(300, 200, 300, 400)
    draw(300, 400, 400, 400)
    draw(300, 200, 400, 200)
    draw(300, 300, 400, 300)
    draw(400, 200, 400, 400)

    draw(100, 200, 250, 400)
    draw(100, 400, 250, 400)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"18101478")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
