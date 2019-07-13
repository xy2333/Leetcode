# -*- coding:utf-8 -*-
class Solution:
	def FindGreatestSumOfSubArray(self, array):
		# write code here
		if len(array) == 0:
			return
		if len(array) == 1:
			return sum(array)
		maxsum = dynamic_max = array[0]
		for i in range(1,len(array)):
			if dynamic_max <= 0:
				dynamic_max = array[i]
			else:
				dynamic_max += array[i]
			if dynamic_max > maxsum:
				maxsum = dynamic_max
		return maxsum

s = [1,-2,3,10,-4,7,2,-5]
t = Solution()
a = t.FindGreatestSumOfSubArray(s)
print(a)
