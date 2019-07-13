# -*- coding:utf-8 -*-
class Solution:
	def FirstNotRepeatingChar(self, s):
		# write code here
		if len(s) == 0:
			return -1
		d = {}
		for i in s:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
		for j in s:
			if d[j] == 1:
				return s.index(j)
		return -1

s = 'google'
t = Solution()
a = t.FirstNotRepeatingChar(s)
print(a)
