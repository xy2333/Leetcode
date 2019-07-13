# -*- coding:utf-8 -*-
class Solution:
	def maxInWindows(self, num, size):
		# write code here
		if size > len(num) or size == 0:
			return []
		index = []
		maxnum = []
		for i in range(len(num)):
			while len(index) >0 and num[i] > num[index[-1]]:
				index.pop()
			index.append(i)
			if index[0] <= i-size:
				index.pop(0)
			maxnum.append(index[0])
		return list(map(lambda x:num[x],maxnum[size-1:]))

s = [2,3,4,2,6,2,5,1]
t = Solution()
a = t.maxInWindows(s,3)
print(a)