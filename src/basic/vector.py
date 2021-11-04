#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from __future__ import annotations
from math import (
    sqrt,
    pow
)

# project dependencies
from src.basic.point import Point

__author__ = "Henrique Kops & Gabriel Castro"


class Vector:

    """
    Vector class
    """

    def __init__(self, p1:Point=None, p2:Point=None) -> None:
        if p1 and p2:
            self.x = (p2.x - p1.x)
            self.y = (p2.y - p1.y)

    def __repr__(self) -> str:
        """
        String representation of this point
        """
        return f"x={self.x} y={self.y}"

    def horizontal(self) -> None:
        """
        Set this vector as unitary horizontally
        """
        self.x = 1.0
        self.y = 0.0

    def dot(self, v: Vector) -> float:
        """
        Dot product between two vectors
        """
        return ((self.x * v.x) + (self.y * v.y))

    def unitary(self) -> None:
        """
        Set this vector as unitary
        """
        self.x = self.x/self.module()
        self.y = self.y/self.module()

    def module(self) -> float:
        """
        Get the module of this vector
        """
        return sqrt((pow(self.x, 2) + pow(self.y, 2)))
