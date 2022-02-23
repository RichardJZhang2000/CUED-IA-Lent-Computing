# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the analysis module"""

from floodsystem.analysis import polyfit

def test_polyfit():
    poly, d0 = polyfit([1,2,3],[1,2,3],3)