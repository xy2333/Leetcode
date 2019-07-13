# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
	def FindNumsAppearOnce(self, array):
		# write code here
		from functools import reduce
		a = reduce(lambda x,y:x^y, array)
		stra = list(bin(a))
		length = len(stra)
		while stra[-1] != '1':
			stra.pop()
		index = length-len(stra)+1
		i = j = 0
		while j < len(array):
			if bin(array[j])[-index] == '1':
				array[i],array[j] = array[j],array[i]
				i += 1
			j += 1
		m = reduce(lambda x,y:x^y, array[:i])
		n = reduce(lambda x,y:x^y, array[i:])
		return [m,n]

s = [2,4,3,6,3,2,5,5]
t = Solution()
a = t.FindNumsAppearOnce(s)
print(a)