# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        # if number == 1:
        # 	return 1
        # if number == 0:
        # 	return 0
        # return self.jumpFloor(number-1) + self.jumpFloor(number-2)
        if number == 1:
        	return 1
        if number == 0:
        	return 0
        last1 = 1
        last2 = 1
        for i in range(2,number+1):
        	now = last1+last2
        	last2 = last1
        	last1 = now
        return now





t = Solution()
a = t.jumpFloor(5)
print(a)
