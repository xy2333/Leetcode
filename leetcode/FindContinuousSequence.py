# -*- coding:utf-8 -*-
class Solution:
	def FindContinuousSequence(self, tsum):
		# write code here
		i = 1
		j = 2
		res = []
		while i < j:
			sum_ij = self.sum(i, j)
			if sum_ij == tsum:
				res.append(list(range(i,j+1)))
				i += 1
			elif sum_ij > tsum:
				i += 1
			else:
				j += 1
		return res

	def sum(self,i,j):
		return sum(list(range(i,j+1)))


s = 15
t = Solution()
a = t.FindContinuousSequence(s)
print(a)