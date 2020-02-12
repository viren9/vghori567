import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),('Right'))
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), ('Right'))
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(1,3,4),('invalidTringle'))
        
    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1,1,1),('Equilateral'))
    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(1, 3, 3), ('Equilateral'))

    def testIsoscelesTriangleA(self):
        self.assertEqual(check_triangle(2, 3, 2), ('Isosceles triangle'))
    def testIsoscelesTriangleB(self):
        self.assertEqual(check_triangle(3, 3, 3), ('Equilateral triangle'))
    def testIsoscelesTriangleC(self):
        self.assertEqual(# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),('Right'))
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), ('Right'))
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(1,3,4),('invalidTringle'))
        
    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1,1,1),('Equilateral'))
    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(1, 3, 3), ('Equilateral'))

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 3, 2), ('Isosceles triangle'))
    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(3, 3, 3), ('Equilateral triangle'))
    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(201, 3, 6), ('invalid triangle'))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

(201, 3, 6), ('invalid triangle'))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

