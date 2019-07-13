# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        s = array
        if len(s) == 0:
        	return False
        lie = len(s)
        row = len(s[0])
        i = 0
        j = lie-1
        while i <= row-1 and j >= 0:
        	if s[j][i] > target:
        		j -= 1
        	elif s[j][i] < target:
        		i += 1
        	else:
        		return True
        return False




s = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
num= 16
t = Solution()
a=t.Find(num,s)
print(a)