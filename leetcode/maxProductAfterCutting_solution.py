# -*- coding:utf-8 -*-
class Solution:
    def maxProductAfterCutting_solution1(self,length):
    	if length == 0:
    		return 0
    	if length == 1:
    		return 0
    	if length == 2:
    		return 1
    	if length == 3:
    		return 2
    	product = [None]*(length+1)
    	product[0],product[1],product[2],product[3] = 0,1,2,3
    	for i in range(4,length+1):
    		pmax = 0
    		for j in range(1,i//2+1):
    			temp = product[j]*product[i-j]
    			if temp > pmax:
    				pmax = temp
    		product[i] = pmax
    	return product[length]

t = Solution()
a = t.maxProductAfterCutting_solution1(8)
print(a)
