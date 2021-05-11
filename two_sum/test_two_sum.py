from two_sum import Solution
import unittest

class TestTwoSum(unittest.TestCase):

	def test_sums_to_9(self):
		s = Solution()
		self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])

	def test_sums_to_6(self):
		s = Solution()
		self.assertEqual(s.twoSum([3,2,4], 6), [1,2])

	def test_sums_to_6_(self):
		s = Solution()
		self.assertEqual(s.twoSum([3,3], 6), [0, 1])
