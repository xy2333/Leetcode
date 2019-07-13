# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent == 0:
        	raise ValueError('in 0**0')
        if exponent == 0:
        	return 1
        if base == 0:
        	if exponent > 0:
        		return 0
        	else:
        		raise ValueError('in 0**(fushu)')
        if exponent > 0:
        	result = 1
        	while exponent > 0:
        		result *= base
        		exponent -= 1
        	return result
        if exponent < 0:
        	result = 1
        	exponent = abs(exponent)
        	while exponent > 0:
        		result *= base
        		exponent -= 1
        	return 1/result

 

t = Solution()
a = t.Power(2,2)
print(a)