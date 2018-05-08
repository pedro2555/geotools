"""
Geo Tools
Copyright (C) 2018  Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of Geo Tools.

Geo Tools is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Geo Tools is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Geo Tools.  If not, see <http://www.gnu.org/licenses/>.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from ddt import ddt, data, unpack

from geo_tools import dms2dd


@ddt
class TestCoordinate(unittest.TestCase):
    @data(
        ('N', 38, 57, 38.000),
        ('W', 9, 11, 4.000),
    )
    @unpack
    def test_dms2dd_(self, direction, degrees, minutes, seconds):
        test = dms2dd(direction, degrees, minutes, seconds)
        # South and West return negative degrees
        if direction == 'S' or direction == 'W':
            self.assertTrue(test <= 0)
        else:
            self.assertTrue(test >= 0)
        self.assertIsInstance(test, float)
