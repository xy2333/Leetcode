# -*- coding:utf-8 -*-
class Solution:
	def IsContinuous(self, numbers):
		# write code here
		if len(numbers) == 0:
			return False
		numbers.sort()
		interval = 0
		for i in range(5):
			if numbers[i] != 0:
				break
		num_0 = i
		while i < 4:
			if numbers[i] == numbers[i+1]:
				return False
			while numbers[i]+1 != numbers[i+1] :
				interval += 1
				numbers[i] += 1
			i += 1

		return interval <= num_0


s = [0,0,1,3,5]
t = Solution()
a = t.IsContinuous(s)
print(a)