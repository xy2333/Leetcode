# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
        	return None
        if len(rotateArray) == 1:
        	return rotateArray
        if len(rotateArray) == 2:
        	return rotateArray[1]
        index1 = 0
        index2 = len(rotateArray)-1
        if rotateArray[index1] < rotateArray[index2]:
        	return rotateArray[index1]
        mid = (index1+index2)//2
        if rotateArray[index1] == rotateArray[index2] == rotateArray[mid]:
        	return inorder(rotateArray)
        if rotateArray[mid] >= rotateArray[index1]:
        	return self.minNumberInRotateArray(rotateArray[mid:])
        else:
        	return self.minNumberInRotateArray(rotateArray[:mid+1])
# 灵性答案
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)
        if length == 0:
            return 0
        if length == 1:
            return rotateArray[0]
        left, right = 0, length- 1
         
        while left<= right:
            mid = (left+ right) >> 1
            if rotateArray[mid] > rotateArray[right]:
                left = mid+ 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1
            if left >= right:
                break
        return rotateArray[left]


t = Solution()
s = [3,4,5,1,2]
a = t.minNumberInRotateArray(s)
print(a)