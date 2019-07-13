# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self,x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
        	return None
        if len(pre) == 1:
        	return TreeNode(pre[0])
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:index+1],tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
        return root






        
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
t = Solution()
a = t.reConstructBinaryTree(pre,tin)
