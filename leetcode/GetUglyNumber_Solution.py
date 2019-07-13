# -*- coding:utf-8 -*-
class Solution:
	def GetUglyNumber_Solution(self, index):
		# write code here
		if index == 0:
			return 0
		ugly = [None]*index
		ugly[0] = 1
		T2 = T3 = T5 =  0
		for i in range(1,index):
			while ugly[T2]*2 <= ugly[i-1]:
				T2 += 1
			while ugly[T3]*3 <= ugly[i-1]:
				T3 += 1
			while ugly[T5]*5 <= ugly[i-1]:
				T5 += 1
			ugly[i] = min(ugly[T2]*2,ugly[T3]*3,ugly[T5]*5)
		return ugly[-1]

s = 0
t = Solution()
a = t.GetUglyNumber_Solution(s)
print(a)