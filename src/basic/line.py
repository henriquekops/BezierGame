#!/usr/bin/env python
#-*- coding: utf-8 -*-

# project dependencies
from src.basic.point import Point

# external dependencies
from OpenGL.GL import (
    glBegin,
    GL_LINES,
    glVertex2f,
    glEnd
)

__author__ = "Henrique Kops & Gabriel Castro"


class Line:

    """
    Line class
    """

    def __init__(self, x1:float, y1:float, x2:float, y2:float) -> None:
        self.p1 = Point(x=x1, y=y1)
        self.p2 = Point(x=x2, y=y2)

    def draw(self) -> None:
        """
        Draw this line
        """
        glBegin(GL_LINES)

        glVertex2f(self.p1.x, self.p1.y)
        glVertex2f(self.p2.x, self.p2.y)

        glEnd()
