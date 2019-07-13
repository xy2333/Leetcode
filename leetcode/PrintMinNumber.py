# -*- coding:utf-8 -*-
class Solution:
	def PrintMinNumber(self, numbers):
		# write code here
		from functools import reduce 
		if not numbers:
			return ''
		numbers = list(map(str,numbers))
		self.quick_sort(numbers)
		return reduce(lambda x,y: x+y, numbers)

	def compare(self, a, b):
		if a == b:
			return 0
		for i in range(min(len(a), len(b))):
			if int(a[i]) > int(b[i]):
				return 1
			elif int(a[i]) < int(b[i]):
				return -1
		if len(a) < len(b):
			b = b[len(a):]
		else:
			a = a[len(b):]
		return self.compare(a, b)

	def quick_sort(self,lst):
		def qsort_rec(lst,begin,end):
			if begin+1 >= end:
				return
			r = lst[begin]
			i = begin
			for j in range(i,end):
				if self.compare(lst[j],r) == -1:
					i += 1
					lst[i],lst[j] = lst[j],lst[i]
			lst[i],lst[begin] = lst[begin],lst[i]
			qsort_rec(lst,begin,i)
			qsort_rec(lst,i+1,end)
	
		qsort_rec(lst,0,len(lst))

s = [3, 32,321]
t = Solution()
a = t.PrintMinNumber([])
print(a)
