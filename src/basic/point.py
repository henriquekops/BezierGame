#!/usr/bin/env python
#-*- coding: utf-8 -*-

# external dependencies
from OpenGL.GL import (
    glBegin,
    GL_POINTS,
    glVertex2f,
    glEnd
)

__author__ = "Henrique Kops & Gabriel Castro"


class Point:

    """
    Point class
    """

    def __init__(self, x:int=0, y:int=0) -> None:
        self.x = x
        self.y = y

    def draw(self) -> None:
        """
        Draw this point
        """
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()
