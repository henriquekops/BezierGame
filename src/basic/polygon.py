#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from typing import Tuple

# project dependencies
from src.basic.point import Point

# external dependencies
from OpenGL.GL import (
    glBegin,
    glEnd,
    glVertex2f,
    glColor3f,
    GL_LINE_LOOP,
    GL_LINES
)

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"


class Polygon:

    def __init__(self) -> None:
        self.vertices = []

    def add(self, x:float, y:float) -> None:
        """
        Add vertex to this polygon
        """
        self.vertices.append(Point(x, y))

    def axis(self) -> None: # TODO: Drop later
        """
        Draw world axes
        """
        glColor3f(1,1,1)
        glBegin(GL_LINES)
        glVertex2f(0, 50)
        glVertex2f(100, 50)
        glVertex2f(50, 0)
        glVertex2f(50, 100)
        glEnd()

    def draw(self) -> None:
        """
        Draw this polygon
        """
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_LINE_LOOP)
        v:Point
        for v in self.vertices:
            glVertex2f(v.x, v.y)
        glEnd()

    def get_limits(self) -> Tuple[Point, Point]:
        """
        Get limits of this polygon
        """
        min:Point = self.vertices[0]
        max:Point = self.vertices[0]
        v:Point
        for v in self.vertices:
            if min.x > v.x: min.x = v.x
            if min.y > v.y: min.y = v.y
            if max.x < v.x: max.x = v.x
            if max.y < v.y: max.y = v.y
        return min, max

    def generate(self, f_path) -> None:
        f = open(f_path)
        n_vertices = int(f.readline())
        for l in f.readlines():
            axis  = l.split()
            x = float(axis[0])
            y = float(axis[1])
            self.add(x, y)
        f.close()
        return self.get_limits()
