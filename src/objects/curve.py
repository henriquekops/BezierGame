#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from math import (
    pow,
    sqrt
)

# project dependencies
from src.basic.point import Point

# external dependencies
from OpenGL.GL import (
    glBegin,
    GL_LINES,
    glVertex2f,
    glColor3f,
    glEnd
)


__author__ = "Henrique Kops & Gabriel Castro"


class Curve:
    """
    Curve class
    """

    def __init__(self, p0:Point, p1:Point, p2:Point, id:int) -> None:
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.id = id
        self.r = 0.0
        self.g = 0.0
        self.b = 0.0

    def __repr__(self) -> str:
        return f"id={self.id} p1=[{self.p0}] p2=[{self.p1}] p3=[{self.p2}]"

    def length(self) -> float:
        dt = 1.0/50
        t = dt
        length = 0
        p1 = self.bezier(0.0)
        while( t < 1.0):
            p2 = self.bezier(t)
            length += self.__distance(p1, p2)
            p1 = p2
            t += dt
        p2 = self.bezier(1.0)
        length += self.__distance(p1, p2)
        return length

    def draw(self) -> None:
        dt = 1.0/50
        t = dt
        p1 = self.bezier(0.0)
        glBegin(GL_LINES)
        glColor3f(self.r, self.g, self.b)
        while( t < 1.0):
            p2 = self.bezier(t)
            glVertex2f(p1.x, p1.y)
            glVertex2f(p2.x, p2.y)
            p1 = p2
            t += dt
        glEnd()
        p2 = self.bezier(1.0)

    def bezier(self, t:float) -> Point:
        mt = 1-t
        x = (pow(mt,2) * self.p0.x) + (2 * mt * t * self.p1.x) + (pow(t, 2) * self.p2.x)
        y = (pow(mt,2) * self.p0.y) + (2 * mt * t * self.p1.y) + (pow(t, 2) * self.p2.y)
        return Point(x, y)

    def __distance(self, p1:Point, p2:Point) -> None:
        return sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))
