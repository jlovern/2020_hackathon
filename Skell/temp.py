# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:25:02 2020

@author: Jakob
"""


def perlin(x,y,z):
    xu = x-int(x)
    yu = y-int(y)
    zu = z-int(z)
    return [xu,yu,zu]
