# -*- coding:utf-8 -*-
class Solution:
	def ReverseSentence(self, s):
		# write code here
		from functools import reduce
		slst = s.split(' ')
		rs = slst[::-1]
		return reduce(lambda x,y:x+' '+y,rs)

s = 'abc'
t = Solution()
a = t.ReverseSentence(s)
print(a)
