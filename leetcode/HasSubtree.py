# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None:
        	return False
        return self.preorder(pRoot1,pRoot2)

    def preorder(self,t,pRoot2):
    	if t is None:
    		return False
    	return self.DoesTree1haveTree2(t,pRoot2) or self.preorder(t.left,pRoot2) or self.preorder(t.right,pRoot2)

    def DoesTree1haveTree2(self,pRoot1,pRoot2):
    	if pRoot2 is None:
    		return True
    	if pRoot1 is None:
    		return False
    	if pRoot1.val == pRoot2.val:
    		return self.DoesTree1haveTree2(pRoot1.left,pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right,pRoot2.right)
    	else:
    		return False

Tree1 = TreeNode(8, TreeNode(8,TreeNode(9),TreeNode(2,TreeNode(4),TreeNode(7))), TreeNode(7))
Tree2 = TreeNode(8, TreeNode(9), TreeNode(2))
t = Solution()
a = t.HasSubtree(Tree1,Tree2)
print(a)