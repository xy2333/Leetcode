# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
        	return False
        return self.rec(sequence)

    def rec(self,sequence):
        if len(sequence) <=  2:
        	return True
        root = sequence[-1]
        index = 0
        for i in range(len(sequence)):
        	if sequence[i] >= root:
        		index = i
        		break
       	for j in sequence[index:-1]:
       		if j < root:
       			return False
       	left = sequence[:index]
       	right = sequence[index:-1]
       	return self.rec(left) and self.rec(right)


# s = [5,7,6,9,11,10,8]
# s = [7,4,6,5]
s = []
t = Solution()
a = t.VerifySquenceOfBST(s)
print(a)
