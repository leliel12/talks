#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skcriteria import moora

mtx = [
    [300, 150, 8],
    [310, 178, 9],
    [280, 130, 10],
]
criteria = [ 1, -1, 1]
moora.multimoora(mtx, criteria)
