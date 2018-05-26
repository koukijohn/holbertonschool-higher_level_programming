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

    def setUp(self):
        """ This function redirects to stdout and checks
        the output of functions relying on print. """

        sys.stdout = StringIO()

    def tearDown(self):
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
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base(12)
        base5 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
        self.assertEqual(base4.id, 12)
        self.assertEqual(base5.id, 4)

    def test_1_id(self):
        """ This test checks after it runs a set of ids. """

        Base._Base__nb_objects = 0
        base = Base()
        self.assertEqual(base.id, 1)

    def test_2_id(self):
        """ This checks to see if the random arguments passed fail or not. """

        Base._Base__nb_objects = 0
        test1 = Base(22)
        self.assertEqual(test1.id, 22)
        test2 = Base(-33)
        self.assertEqual(test2.id, -33)
        test3 = Base()
        self.assertEqual(test3.id, 1)

    def test_3_set_nb(self):
        """ This checks to see if nb_objects is set as private. """

        base = Base(33)
        with self.assertRaises(AttributeError):
            print(base.nb_objects)
        with self.assertRaises(AttributeError):
            print(base.__nb_objects)

    def test_4_dictionary(self):
        """ This test checks to see if the dictionary
        is working. """

        rectangle = Rectangle(10, 7, 2, 8, 1)
        dictionary = rectangle.to_dictionary()
        j = {'x': 2, 'id': 1, 'y': 8, 'height': 7, 'width': 10}
        jd = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, j)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(jd), str)

    def test_6_from_json_string(self):
        """ This test checks to see if from_json_to_string works or not. """

        s = '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}, \
{"id": 10, "width": 12, "height": 14, "x": 16, "y": 18}]'
        js = Base.from_json_string(s)
        self.assertTrue(type(js) is list)
        self.assertEqual(len(js), 2)

    def test_7_from_json_string_if_empty(self):
        """ This test checks to see if it works with
        an empty string or none. """

        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_10_rectangle(self):
        """ This test checks for rectangle creation. """

        Rectangle1 = Rectangle(4, 5, 6)
        Rectangle1_dict = Rectangle1.to_dictionary()
        Rectangle2 = Rectangle.create(**Rectangle1_dict)
        self.assertNotEqual(Rectangle1, Rectangle2)

    def test_11_square(self):
        """ This test checks for the square creation. """

        Square1 = Square(44, 55, 66, 77)
        Square1_dict = Square1.to_dictionary()
        Square2 = Rectangle.create(**Square1_dict)
        self.assertNotEqual(Square1, Square2)

    def test_12_file_rectangle(self):
        """ This test checks if the file loads from rectangle. """

        Rectangle1 = Rectangle(33, 34, 35, 26)
        Rectangle2 = Rectangle(202, 2)
        loadRectangle = [Rectangle1, Rectangle2]
        Rectangle.save_to_file(loadRectangle)
        loadRectangle2 = Rectangle.load_from_file()
        self.assertNotEqual(loadRectangle, loadRectangle2)

    def test_13_file_square(self):
        """ This test checks to see if the file loads from square. """

        Square1 = Square(22)
        Square2 = Square(44, 44, 55, 66)
        loadSquare = [Square1, Square2]
        Square.save_to_file(loadSquare)
        loadSquare2 = Square.load_from_file()
        self.assertNotEqual(loadSquare, loadSquare2)
