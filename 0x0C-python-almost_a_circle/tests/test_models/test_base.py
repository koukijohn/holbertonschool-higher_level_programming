#!/usr/bin/python3
""" This module contains all of the unittest for the Base class. """
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO
import json
import os


class TestBase(unittest.TestCase):
    """ This class contains all of our unittest for Base. """

    def setup(self):
        """ This function redirects to stdout and checks
        the output of functions relying on print. """

        sys.stdout = StringIO()

    def cleaner(self):
        """ This tearsDown/cleans everything up after running
        the setup. """

        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """ This tests for pep8. """

        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """ This tests for pep8. """

        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """ This test if d it's a docstring. """

        self.assertIsNotNone(Base.__doc__)

    def test_00_documentation(self):
        """ This tests to see if the documentation is
        created and if it's correct. """

        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(Base.load_from_file.__doc__)

    def test_0_id(self):
        """ This test checks for the id method. """

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_1_id(self):
        """ This test checks after it runs a set of ids. """

        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)

    def test_2_id(self):
        """ This checks to see if the random arguments passed fail or not. """

        Base._Base__nb_objects = 0
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 1)

    def test_3_set_nb(self):
        """ This checks to see if nb_objects is set as private. """

        b = Base(33)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_4_dict(self):
        """ This test checks to see if the dictionary
        is working. """

        r1 = Rectangle(10, 7, 2, 8, 1)
        d1 = r1.to_dictionary()
        j = {'x': 2, 'id': 1, 'y': 8, 'height': 7, 'width': 10}
        jd = Base.to_json_string([d1])
        self.assertEqual(d1, j)
        self.assertEqual(type(d1), dict)
        self.assertEqual(type(jd), str)

    def test_6_from_json_string(self):
        """ This test checks to see if from_json_to_string works or not. """

        s = '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}, \
{"id": 10, "width": 12, "height": 14, "x": 16, "y": 18}]'
        js = Base.from_json_string(s)
        self.assertTrue(type(js) is list)
        self.assertEqual(len(js), 2)

    def test_7_from_json_string_empty(self):
        """ This test checks to see if it works with
        an empty string or none. """

        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_10_rect(self):
        """ This test checks for rectangle creation. """

        R1 = Rectangle(4, 5, 6)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def test_11_sq(self):
        """ This test checks for the square creation. """

        S1 = Square(44, 55, 66, 77)
        S1_dict = S1.to_dictionary()
        S2 = Rectangle.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def test_12_file_rect(self):
        """ This test checks if the file loads from rect. """

        R1 = Rectangle(33, 34, 35, 26)
        R2 = Rectangle(202, 2)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_13_file_square(self):
        """ This test checks to see if the file loads from square. """

        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)
