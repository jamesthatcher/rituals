

class Solution(object):

	def in_both(self, sorted1, sorted2):
		in_both = []

		# iterate through sorted1 and find which values match those in sorted2
		for i in sorted1:
			if i in sorted2:
				in_both.append(i)

		# iterate through sorted2 and find which values match those in sorted1
		for i in sorted2:
			if i in sorted1:
				in_both.append(i)

		# only return unique values
		return list(set(in_both))

