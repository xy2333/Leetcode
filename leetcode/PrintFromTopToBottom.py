# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        deque = []
        res = []
        if root is None:
            return []
        deque.append(root)
        while len(deque) > 0:
            temp = deque.pop(0)
            res.append(temp.val)
            if temp.left is not None:
                deque.append(temp.left)
            if temp.right is not None:
                deque.append(temp.right)
        return res


Tree1 = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)),TreeNode(10, TreeNode(9), TreeNode(11)))
t = Solution()
a = t.PrintFromTopToBottom(Tree1)
print(a)
