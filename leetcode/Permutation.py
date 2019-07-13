# -*- coding:utf-8 -*-
class Solution:
	def Permutation(self, ss):
		# write code here
		if len(ss) == 0:
			return []
		lstr = list(ss)
		res = self.rec(lstr)
		return sorted(list(set(res)))


	def rec(self,lstr):
		if len(lstr) == 0:
			return
		if len(lstr) == 1:
			return lstr
		res = []
		for i in range(len(lstr)):
			temp = list(lstr)
			temp.pop(i)
			lastPermutation = self.rec(temp)
			res += self.linklist(lstr[i],lastPermutation)
		return res

	def linklist(self,a,b):
		res = []
		for i in b:
			res.append(a+i)
		return res

s = 'aab'
t = Solution()
a = t.Permutation(s)
print(a)