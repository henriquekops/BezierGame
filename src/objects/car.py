#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from math import (
    acos,
    cos,
    sin
)

# project dependencies
from src.basic.polygon import Polygon
from src.basic.vector import Vector
from src.objects.curve import Curve

__author__ = "Henrique Kops & Gabriel Castro"


class Car(Polygon):

    """
    Car class
    """

    __DEGREE = 180/3.14159265

    def __init__(self) -> None:
        super().__init__()
        self.position = None
        self.rotation = 0.0
        self.curve = None
        self.velocity = 100
        self.a_t = 0.0
        self.b_t = 0.0

    def set_curve(self, curve:Curve) -> None:
        self.curve = curve
        self.position = curve.p0

    def move(self, dt:float) -> None:
        if dt == 0: dt = 0.000000001
        deslocation = self.velocity * dt
        pos = deslocation/self.curve.length()
        self.b_t = self.a_t
        self.a_t = self.a_t + pos
        self.position = self.curve.bezier(self.a_t)

    def direction(self) -> float:
        p1 = self.curve.bezier(self.b_t)
        p2 = self.curve.bezier(self.a_t)
        v_dir = Vector(p2, p1)
        v_dir.unitary()
        v_hor = Vector()
        v_hor.x = 1.0
        v_hor.y = 0.0
        rotation = self.__DEGREE * acos(v_dir.dot(v_hor))
        if v_dir.y < 0: rotation = -rotation
        self.rotation = rotation
