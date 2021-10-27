#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from math import pow

# project dependencies
from src.basic.point import Point

__author__ = "Henrique Kops & Gabriel Castro"


class Curve:
    """
    Curve class
    """

    def __init__(self, p0:Point, p1:Point, p2:Point) -> None:
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.curve_calcuation()

    def curve_calcuation(self) -> None:
        dt = 1.0/50
        t = dt
        length = 0
        p1 = self.bezier(0.0)
        while( t < 1.0):
            p2 = self.bezier(t)
            # length += distance(p1, p2)
            p1 = p2
            t += dt
        p2 = self.bezier(1.0)
        # length += distance(p1, p2)
        print(length)

    def bezier(self, t:float) -> float:
        mt = 1-t
        return (pow(mt,2) * self.p0) + ((2 * (mt * t)) * self.p1) + (pow(t, 2) * self.p2)

    def distance(self, p1:Point, p2:Point) -> None:
        # TODO
        pass
