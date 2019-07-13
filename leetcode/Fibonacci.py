# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # if n == 0:
        # 	return 0
        # elif n == 1:
        # 	return 1
        # else:
        # 	return self.Fibonacci(n-1)+self.Fibonacci(n-2)
        if n == 0:
        	return 0
        if n == 1:
        	return 1
        last1 = 1
        last2 = 0
        i = 2
        while i <= n:
        	now = last1+last2
        	last2 = last1
        	last1 = now
        	i += 1
        return last1


t = Solution()
a = t.Fibonacci(5)
print(a)
