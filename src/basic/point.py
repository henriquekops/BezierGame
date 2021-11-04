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

    def __init__(self, x:float=0.0, y:float=0.0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        String representation of this point
        """
        return f"x={self.x} y={self.y}"

    def draw(self) -> None:
        """
        Draw this point
        """
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()
