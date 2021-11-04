#!/usr/bin/env python
#-*- coding: utf-8 -*-

# built-in dependencies
from random import (
    randint,
    random
)
from typing import Tuple

# project dependencies
from src.objects.curve import Curve
from src.basic.polygon import Polygon
from src.basic.point import Point


class Map(Polygon):

    def __init__(self) -> None:
        super().__init__()
        self.curves = []
        self.first = True

    def draw_curves(self) -> None:
        c: Curve
        for c in self.curves:
            if self.first:
                c.r = random()
                c.g = random()
                c.b = random()
            c.draw()
        self.first = False

    def add_curve(self, curve:Curve) -> None:
        self.curves.append(curve)

    def get_next(self, curve:Curve, forward:bool) -> Tuple[Curve, bool]:
        aux = []
        c:Curve
        for c in self.curves:
            if c.id != curve.id:
                if forward:
                    if curve.p2.id() == c.p0.id():
                        aux.append((c, True))
                    elif curve.p2.id() == c.p2.id():
                        aux.append((c, False))
                else:
                    if curve.p0.id() == c.p0.id():
                        aux.append((c, True))
                    elif curve.p0.id() == c.p2.id():
                        aux.append((c, False))
        return aux[randint(0,len(aux)-1)]

    def render(self, f_path) -> None:
        f = open(f_path)
        id = 0
        for l in f.readlines():
            points = l.split()
            p1 = int(points[0])
            p2 = int(points[1])
            p3 = int(points[2])
            self.add_curve(Curve(self.vertices[p1], self.vertices[p2], self.vertices[p3], id))
            id += 1