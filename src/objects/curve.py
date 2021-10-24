#!/usr/bin/env python
#-*- coding: utf-8 -*-

from src.basic.point import Point

__author__ = "Henrique Kops & Gabriel Castro"


class Curve:
    """
    Curve class
    """

    def __init__(self, P0:Point, P1:Point, P2:Point) -> None:

        self.P[0] = P0
        self.P[1] = P1
        self.P[2] = P2
        self.curve_calcuation()
        pass

    def curve_calcuation(self) -> None:

        dt = 1.0/50 # dt - delta T
        t = dt
        tc = 0 #tc - comprimento total da curva
        p1 = self.bezier_calculation(0.0)
        while( t < 1.0):
            p2 = self.bezier_calculation(t)
            #tc += calcula_distancia(p1,p2)
            p1 = p2
            t += dt 
        p2 = self.bezier_calculation(1.0)
        #tc += calcula_distancia(p1,p2)



        pass

    def bezier_calculation(self, t:float) -> Point:
        mt = 1-t

        P = self.P[0] * mt  * mt + self.P[1] * 2 * mt * t + self.P[2] * t * t

        return P




"""
void Bezier::calculaComprimentoDaCurva()
{
    double DeltaT = 1.0/50;
    double t=DeltaT;
    Ponto P1, P2;
    ComprimentoTotalDaCurva = 0;
    P1 = Calcula(0.0);
    while(t<1.0)
    {
        P2 = Calcula(t);
        ComprimentoTotalDaCurva += calculaDistancia(P1,P2);
        P1 = P2;
        t += DeltaT;
    }
    P2 = Calcula(1.0); // faz o fechamento da curva
    ComprimentoTotalDaCurva += calculaDistancia(P1,P2);
    cout << "ComprimentoTotalDaCurva: " << ComprimentoTotalDaCurva << endl;
}
"""
