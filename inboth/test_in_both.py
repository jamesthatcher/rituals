from in_both import Solution

import unittest

class TestInBoth(unittest.TestCase):

	def test_in_both_equality(self):
		s = Solution()
		self.assertEqual(s.in_both([1, 2, 3, 4], [1, 2, 3, 4]), [1, 2, 3, 4])

	def test_in_both_inequality(self):
		s = Solution()
		self.assertEqual(s.in_both([1, 2, 3, 4], []), [])

	def test_in_both_single(self):
		s = Solution()
		self.assertEqual(s.in_both([1, 2, 3, 4], [1]), [1])

	def test_in_both_duplicates1(self):
		s = Solution()
		self.assertEqual(s.in_both([1, 2, 3, 4], [1, 1]), [1])

	def test_in_both_duplicates2(self):
		s = Solution()
		self.assertEqual(s.in_both([1, 1], [1, 2, 3, 4]), [1])