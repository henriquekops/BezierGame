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


class Vector:

    def __init__(self, p1:Point=None, p2:Point=None) -> None:
        if p1 and p2:
            self.x = (p2.x - p1.x)
            self.y = (p2.y - p1.y)

    def __repr__(self) -> str:
        return f"x={self.x} y={self.y}"

    def dot(self, v: Vector) -> float:
        return ((self.x * v.x) + (self.y * v.y))

    def unitary(self) -> None:
        self.x = self.x/self.module()
        self.y = self.y/self.module()

    def module(self) -> float:
        return sqrt((pow(self.x, 2) + pow(self.y, 2)))
