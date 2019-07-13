# -*- coding:utf-8 -*-
class Solution:
	def NumberOf1Between1AndN_Solution(self, n):
		# write code here
		nstr = str(n)
		length = len(nstr)
		if length == 1:
			if n == 0:
				return 0
			else:
				return 1
		newstr = nstr[1:]
		if newstr == '':
			newstr = '0'
		if nstr[0] != '1':
			num = 10**(length-1)
		else:
			num = n-10**(length-1)+1
		return num + int(nstr[0])*(length-1)*10**(length-2) + self.NumberOf1Between1AndN_Solution(int(newstr))

s = 10
t = Solution()
a = t.NumberOf1Between1AndN_Solution(s)
print(a)
