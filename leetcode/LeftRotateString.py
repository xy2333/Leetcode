# -*- coding:utf-8 -*-
class Solution:
	def LeftRotateString(self, s, n):
		# write code here
		if n > len(s):
			return s
		slst = list(s)
		return s[n:]+s[:n]

s = 'abcdefg'
t = Solution()
a = t.LeftRotateString(s,2)
print(a)