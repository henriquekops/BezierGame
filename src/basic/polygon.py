#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from typing import Tuple
from itertools import combinations

# project dependencies
from src.basic.point import Point

# external dependencies
from OpenGL.GL import (
    glBegin,
    glEnd,
    glVertex2f,
    glColor3f,
    GL_LINE_LOOP
)

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"


class Polygon:

    def __init__(self) -> None:
        self.vertices = []
        self.pairs = []

    def add(self, x:float, y:float) -> None:
        """
        Add vertex to this polygon
        """
        self.vertices.append(Point(x, y))

    def draw(self) -> None:
        """
        Draw this polygon
        """
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_LINE_LOOP)
        for p in self.pairs:
            glVertex2f(p[0].x, p[0].y)
            glVertex2f(p[1].x, p[1].y)
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
        """
        Generates this polygon through text file
        """
        f = open(f_path)
        for l in f.readlines():
            axis  = l.split()
            x = float(axis[0])
            y = float(axis[1])
            self.add(x, y)
        f.close()
        self.pairs = list(combinations(self.vertices, 2))
        # return self.get_limits()
