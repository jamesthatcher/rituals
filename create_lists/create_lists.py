
class Solution(object):

	def create_lists(self, n):
		lists = []
		if n == 0:
			return lists

		for l in range(0, n):
			inner_list = []
			for inner in range(0, l+1):
				inner += 1
				inner_list.append(inner)

			lists.append(inner_list)

		return lists
