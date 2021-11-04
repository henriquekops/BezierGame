#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
import sys
from os import _exit
from time import time
from random import (
    randint,
    choice
)

# project dependencies
from src.objects.car import Car
from src.objects.map import Map

# external dependencies
from OpenGL.GL import (
    glClear,
    glMatrixMode,
    glLoadIdentity,
    glOrtho,
    glViewport,
    glPushMatrix,
    glTranslatef,
    glClearColor,
    glRotatef,
    glPopMatrix,
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
SPACE = b' '

# global variables
past_time = time()
dt, acc_time, n_frames, total_time = 0, 0, 0, 0
num_enemies = 5
mainCar = Car()
map = Map()
enemies = []
dead = False


def init() -> None:
    global enemies, mainCar, map
    enemies = []
    mainCar.set_curve(map.curves[randint(0, len(map.curves)-1)], True)
    for _ in range(num_enemies):
        enemy = Car()
        enemy.generate("config/car.txt")
        enemy.set_curve(map.curves[randint(0, num_enemies)], choice([True, False]))
        enemies.append(enemy)

def check_collision() -> None:
    global enemies, mainCar, dead
    e: Car
    for e in enemies:
        if mainCar.curve.id == e.curve.id:
            if abs(mainCar.a_t - e.a_t) < 0.01:
                dead = True


def display() -> None:
    """
    Draw objects at window
    """
    global mainCar, map, enemies, dead

    if dead:
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClearColor(1, 0, 0, 0)
    else:
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        map.draw_curves()

        display_car(mainCar, 0.0, 1.0, 0.0)
        for e in enemies:
            display_car(e, 1.0, 0.0, 0.0)

        check_collision()

    glutSwapBuffers()


def display_car(car: Car, r, g, b) -> None:
    curve_ended = car.move(dt)

    if curve_ended:
        new_curve, forward = map.get_next(car.curve, car.forward)
        car.set_curve(new_curve, forward)
    else:
        car.direction()
        glPushMatrix()
        glTranslatef(car.position.x, car.position.y, 0)
        glRotatef(car.rotation, 0, 0, 1)
        car.draw(r, g, b)
        glPopMatrix()


def idle() -> None:
    """
    Control program while idle
    """
    global dt, past_time, acc_time, total_time, n_frames
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
    glOrtho(-7, 7, -7, 7, 0, 1)
    glViewport(0, 0, w, h)


def keyboard(*args) -> None:
    """
    Control keyboard input
    """
    if args[0] == ESCAPE: _exit(0)
    elif args[0] == SPACE: init()
    glutPostRedisplay()


def special(a_keys, x:int, y:int) -> None:
    """
    Control special key input
    """
    global mainCar
    if a_keys == GLUT_KEY_UP: mainCar.velocity = 30
    if a_keys == GLUT_KEY_DOWN: mainCar.velocity = 0.1
    if a_keys == GLUT_KEY_LEFT: mainCar.forward = False
    if a_keys == GLUT_KEY_RIGHT: mainCar.forward = True


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
    map.generate("config/map_control.txt")
    map.render("config/map.txt")
    mainCar.generate("config/car.txt")
    init()
    glutMainLoop()
