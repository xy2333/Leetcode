# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n>>i & 1) for i in range(0,32)])

t = Solution()
a = t.NumberOf1(-2147483648)
print(a)