from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def midpoint(r):
    d_init = 1 - r
    d = d_init
    x = 0
    y = r

    points = []
    while(x < y):
        points.append((x, y))
        if d >= 0:
            d += (2*x) - (2*y) + 5
            x = x + 1
            y = y - 1
        else:
            d += (2*x) + 3
            x = x + 1
    return points


# method to map any point to zone 0
def convertToZone0(x, y, sourceZone):
    if sourceZone == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif sourceZone == 'zone 2':
        rx = y
        ry = (-1) * x
        return (rx, ry)
    elif sourceZone == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif sourceZone == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif sourceZone == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif sourceZone == 'zone 6':
        rx = (-1)*y
        ry = x
        return (rx, ry)
    elif sourceZone == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


# method to map zone 0 point to any other zone
def convertToOriginal(x, y, destinationZone):
    if destinationZone == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif destinationZone == 'zone 2':
        rx = (-1) * y
        ry = x
        return (rx, ry)
    elif destinationZone == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif destinationZone == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif destinationZone == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif destinationZone == 'zone 6':
        rx = y
        ry = (-1)*x
        return (rx, ry)
    elif destinationZone == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


def drawCircle(r, x, y):
    glBegin(GL_POINTS)
    zone_1_points = midpoint(r)
    zone_0_points = []
    zone_2_points = []
    zone_3_points = []
    zone_4_points = []
    zone_5_points = []
    zone_6_points = []
    zone_7_points = []

    for (a, b) in zone_1_points:
        zone_0_points.append(convertToZone0(a, b, 'zone 1'))

    for (a, b) in zone_0_points:
        zone_2_points.append(convertToOriginal(a, b, 'zone 2'))
        zone_3_points.append(convertToOriginal(a, b, 'zone 3'))
        zone_4_points.append(convertToOriginal(a, b, 'zone 4'))
        zone_5_points.append(convertToOriginal(a, b, 'zone 5'))
        zone_6_points.append(convertToOriginal(a, b, 'zone 6'))
        zone_7_points.append(convertToOriginal(a, b, 'zone 7'))

    for (a, b) in zone_0_points:
        glVertex2f(a+x, b+y)
    for (a, b) in zone_1_points:
        glVertex2f(a+x, b+y)
    for (a, b) in zone_2_points:
        glVertex2f(a+x, b+y)
    for (a, b) in zone_3_points:
        glVertex2f(a+x, b+y)
    for (a, b) in zone_4_points:
        glVertex2f(a+x, b+y)
    for (a, b) in zone_5_points:
        glVertex2f(a+x, b+y)
    for (a, b) in zone_6_points:
        glVertex2f(a+x, b+y)
    for (a, b) in zone_7_points:
        glVertex2f(a+x, b+y)

    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 1, 0)
    glPointSize(2)

    drawCircle(100, 300, 250)
    drawCircle(50, 350, 250)
    drawCircle(50, 250, 250)
    drawCircle(50, 300, 300)
    drawCircle(50, 300, 200)

    drawCircle(50, 280, 295)

    drawCircle(50, 280, 205)
    drawCircle(50, 320, 295)
    drawCircle(50, 320, 205)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 500)
glutInitWindowPosition(-200, -200)
wind = glutCreateWindow(b"18101478 Lab 03")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
