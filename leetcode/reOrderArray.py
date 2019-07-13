# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray1(self, array):
        # write code here
        if len(array) <= 1:
        	return
        i = 0
        j = len(array)-1
        while 1:
        	while j >= 0 and array[j]%2 != 1:
        		j -= 1
        	while i < len(array) and array[i]%2 != 0:
        		i += 1
        	if i < j:
        		array[i],array[j] = array[j],array[i]
        	else:
        		return
    def reOrderArray2(self, array):
        # write code here
        def isodd(x):
            if x%2 == 0:
                return True
            else:
                return False

        if len(array) <= 1:
            return array
        for i in range(len(array)-1):
            flag = 0
            for j in range(len(array)-i-1):
                if isodd(array[j]) and not isodd(array[j+1]):
                    array[j],array[j+1] = array[j+1],array[j]
                    flag = 1
            if flag == 0:
                return array
        return array




t = Solution()
s = [1,2,3] 
a = t.reOrderArray2(s)
print(a)