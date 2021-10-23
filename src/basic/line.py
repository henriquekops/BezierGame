#!/usr/bin/env python
#-*- coding: utf-8 -*-

# project dependencies
from basic.point import Point
import point

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

    def __init__(self, x1:int, y1:int, x2:int, y2:int) -> None:
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
