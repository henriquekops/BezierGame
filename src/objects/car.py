#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from math import acos

# project dependencies
from src.basic.polygon import Polygon
from src.basic.vector import Vector
from src.objects.curve import Curve

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"


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
        self.velocity = 30
        self.a_t = 0.0
        self.b_t = 0.0
        self.forward = True

    def set_curve(self, curve:Curve, forward:bool) -> None:
        """
        Set the curve for this car to move on
        """
        if forward:
            self.a_t = 0.0
            self.b_t = 0.0
        else:
            self.a_t = 1.0
            self.b_t = 0.0
        self.rotation = 0.0
        self.position = None
        self.curve = curve
        self.forward = forward

    def move(self, dt:float) -> bool:
        """
        Move this car over curve
        """
        if dt == 0: dt = 0.000000001
        if (self.forward and self.a_t < 1.0) or (not self.forward and self.a_t > 0.0):
            velocity = self.velocity
            deslocation = velocity * dt
            pos = deslocation/self.curve.length()
            self.b_t = self.a_t
            if self.forward:
                self.a_t = self.a_t + pos
            else:
                self.a_t = self.a_t - pos
            self.position = self.curve.bezier(self.a_t)
            return False
        return True

    def direction(self) -> None:
        """
        Set the rotation of this car
        """
        p1 = self.curve.bezier(self.b_t)
        p2 = self.curve.bezier(self.a_t)
        v_dir = Vector(p1, p2)
        v_dir.unitary()
        v_hor = Vector()
        v_hor.horizontal()
        rotation = self.__DEGREE * acos(v_dir.dot(v_hor))
        if v_dir.y < 0: rotation = -rotation
        self.rotation = rotation
