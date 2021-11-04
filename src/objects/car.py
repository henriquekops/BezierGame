#!/usr/bin/env python
#-*- coding: utf-8 -*-

# project dependencies
from os import curdir
from src.basic.polygon import Polygon
from src.basic.point import Point
from src.objects.curve import Curve

__author__ = "Henrique Kops & Gabriel Castro"


class Car(Polygon):

    """
    Car class
    """

    def __init__(self) -> None:
        super().__init__()
        self.position = None
        self.curve = None
        self.rotation = 0.0
        self.velocity = 100
        self.t = 0.0

    def set_curve(self, curve:Curve) -> None:
        self.curve = curve
        self.position = curve.p0

    def move(self, dt:float) -> None:
        deslocation = self.velocity * dt
        pos = deslocation/self.curve.length()
        self.t += pos
        self.position = self.curve.bezier(self.t)

    def orientation(self) -> None:
        pass
