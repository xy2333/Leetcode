# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.snum = '0123456789'
		self.error = 1

	def StrToInt(self, s):
    	# write code here
		if len(s) == 0:
			return 0
		if s[0] == '-':
			flag = 1
			res = self.rec(s[1:])
		elif s[0] == '+':
			flag = 0
			res = self.rec(s[1:])
		elif s[0] in self.snum:
			flag = 0
			res = self.rec(s)
		else:
			self.error = 0
		return res*((-1)**flag)*self.error

	def rec(self,s):
		if len(s) == 0:
			return 0
		if s[0] in self.snum:
			return int(s[0])*(10**(len(s)-1))+self.rec(s[1:])
		else:
			self.error = 0
			return 0