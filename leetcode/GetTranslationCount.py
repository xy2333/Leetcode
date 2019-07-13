# -*- coding:utf-8 -*-
class Solution:
	def GetTranslationCount(self, number):
		# write code here
		nstr = str(number)
		if len(nstr) == 1:
			return 1
		elif len(nstr) == 2:
			if number >= 10 and number <= 25:
				return 3
			else:
				return 2
		i = len(nstr)-2
		f_1 = 1
		f_2 = 0
		while i >= 0:
			if int(nstr[i:i+2]) >= 10 and int(nstr[i:i+2]) <= 25:
				g = 1
			else:
				g = 0
			f = f_1 + g*f_2
			f_1,f_2 = f,f_1
			i -= 1
		return f

s = 12258
t = Solution()
a = t.GetTranslationCount(s)
print(a)
