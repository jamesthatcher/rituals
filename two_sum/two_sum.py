# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):

	def twoSum(self, nums, target):
		for pos, n in enumerate(nums):
			for pos2, n2 in enumerate(nums):
				if pos == pos2:
					continue
				if n + n2 == target:
					return [pos, pos2]
