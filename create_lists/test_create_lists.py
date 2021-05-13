from create_lists import Solution

import unittest

class TestCreateLists(unittest.TestCase):

	def test_create_none(self):
		s = Solution()
		self.assertEqual(s.create_lists(0), [])

	def test_create_single(self):
		s = Solution()
		self.assertEqual(s.create_lists(1), [[1]])

	def test_create_double(self):
		s = Solution()
		self.assertEqual(s.create_lists(2), [[1], [1,2]])

	def test_create_triple(self):
		s = Solution()
		self.assertEqual(s.create_lists(3), [[1], [1,2], [1,2,3]])
