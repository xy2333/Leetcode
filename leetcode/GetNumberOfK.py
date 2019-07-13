# -*- coding:utf-8 -*-
class Solution:
	def GetNumberOfK(self, data, k):
		# write code here
		first_k, end_k = self.binarysearch(data,k,0,len(data))
		return end_k - first_k

	def binarysearch(self,data,k,begin,end):
		if begin >= end:
			return 0 , 0
		index = (end-begin)//2+begin
		if data[index] == k:
			if index-1 < begin or data[index-1] != k:
				first_k = index
			else:
				first_k , b = self.binarysearch(data,k,begin,index)
			if index+1 >= end or data[index+1] != k:
				last_k = index+1
			else:
				a , last_k = self.binarysearch(data,k,index+1,end)
			return first_k , last_k
		elif data[index] > k:
			return self.binarysearch(data,k,begin,index)
		else:
			return self.binarysearch(data,k,index+1,end)


s = [1,3,3,3,3,4,5]
t = Solution()
a = t.GetNumberOfK(s,2)
print(a)