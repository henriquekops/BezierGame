#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
import sys
from os import _exit
from time import time

# project dependencies
from src.basic.point import Point
from src.basic.polygon import Polygon
from src.objects.curve import Curve
from src.objects.car import Car

# external dependencies
from OpenGL.GL import (
    glClear,
    glMatrixMode,
    glLoadIdentity,
    glOrtho,
    glViewport,
    GL_PROJECTION,
    GL_COLOR_BUFFER_BIT,
    GL_MODELVIEW
)
from OpenGL.GLUT import (
    glutInit,
    glutCreateWindow,
    glutSwapBuffers,
    glutPostRedisplay,
    glutInitDisplayMode,
    glutInitWindowPosition,
    glutInitWindowSize,
    glutDisplayFunc,
    glutIdleFunc,
    glutReshapeFunc,
    glutKeyboardFunc,
    glutSpecialFunc,
    glutMouseFunc,
    glutMotionFunc,
    glutMainLoop,
    GLUT_RGBA,
    GLUT_KEY_UP,
    GLUT_KEY_DOWN,
    GLUT_KEY_LEFT,
    GLUT_KEY_RIGHT
)

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"


# constants
ESCAPE = b'\x1b'

# global variables
past_time = time()
acc_time, n_frames, total_time = 0, 0, 0
polygon = Polygon()
curve = Curve(Point(0, 35), Point(50,100), Point(100,35))


def display() -> None:
    """
    Draw objects at window
    """
    global polygon, curve
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    polygon.draw()
    polygon.axis()
    curve.draw()
    glutSwapBuffers()


def idle() -> None:
    """
    Control program while idle
    """
    global past_time, acc_time, total_time, n_frames
    now_time = time()
    dt = (now_time - past_time)
    past_time = now_time
    acc_time += dt
    total_time += dt
    n_frames += 1
    if acc_time > 1.0/30: acc_time = 0; glutPostRedisplay()
    if total_time > 5.0: idle_stats(); total_time = 0; n_frames = 0


def idle_stats() -> None:
    """
    Program idle statistics
    """
    global total_time, n_frames
    print(f"""***************************
    Total time: {total_time}
    Frames w/o draw: {int(n_frames)}
    FPS w/o draw: {int(n_frames/total_time)}
    """)


def reshape(w:int, h:int) -> None:
    """
    Redimension OpenGL window
    """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 100, 0, 100, 0, 1)
    glViewport(0, 0, w, h)


def keyboard(*args) -> None:
    """
    Control keyboard input
    """
    if args[0] == ESCAPE: _exit(0)
    glutPostRedisplay()


def special(a_keys, x:int, y:int) -> None:
    """
    Control special key input
    """
    if a_keys == GLUT_KEY_UP: pass
    if a_keys == GLUT_KEY_DOWN: pass
    if a_keys == GLUT_KEY_LEFT: pass
    if a_keys == GLUT_KEY_RIGHT: pass


def mouse(button:int, state:int, x:int, y:int) -> None:
    """
    Control mouse position
    """
    glutPostRedisplay()


def motion(x:int, y:int) -> None:
    """
    Control mouse motion
    """
    glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(700, 500)
    glutInitWindowPosition(100, 100)
    window = glutCreateWindow("Bezier Game")
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    polygon.generate("config/test.txt")
    glutMainLoop()
