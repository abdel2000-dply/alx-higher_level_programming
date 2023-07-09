#!/usr/bin/python3
"""Unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

	"""test"""

	def test_module_docstring(self):
	moduleDoc = __import__('6-max_integer').__doc__
	self.assertTrue(len(moduleDoc) > 1)

	def test_function_docstring(self):
	functionDoc = __import__('6-max_integer').max_integer.__doc__
	self.assertTrue(len(functionDoc) > 1)
