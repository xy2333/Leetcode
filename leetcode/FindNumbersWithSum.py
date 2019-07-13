# -*- coding:utf-8 -*-
class Solution:
	def FindNumbersWithSum(self, array, tsum):
		# write code here
		length = len(array)
		if length <= 1:
			return []
		i = 0
		j = length-1
		res = []
		while i < j:
			if array[i]+array[j] == tsum:
				res.append([array[i],array[j]])
				i += 1
			elif array[i]+array[j] > tsum:
				j -= 1
			else:
				i += 1
		if len(res) == 0:
			return []
		mincross = res[0][0]*res[0][1]
		index = 0
		for k in range(len(res)):
			if res[k][0]*res[k][1] < mincross :
				mincross = res[k][0]*res[k][1]
				index = k
		if res[index][0] > res[index][1] :
			return res[index][1],res[index][0]
		else:
			return res[index][0],res[index][1]



s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
t = Solution()
a = t.FindNumbersWithSum(s,21)
print(a)