# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def Print(self, pRoot):
        # write code here
        deque = []
        res = [[]]
        nowlevel = 0
        nextlevel = 0
        if pRoot is None:
            return []
        deque.append(pRoot)
        nowlevel += 1
        while len(deque) > 0:
            temp = deque.pop(0)
            nowlevel -= 1
            res[-1].append(temp.val)
            if temp.left is not None:
                deque.append(temp.left)
                nextlevel += 1
            if temp.right is not None:
                deque.append(temp.right)
                nextlevel += 1
            if nowlevel == 0:
                nowlevel, nextlevel = nextlevel, nowlevel
                if nowlevel != 0:
                    res.append([])
        for i in range(len(res)):
        	if i%2 == 1:
        		res[i] = res[i][::-1]
        return res

Tree1 = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)),
                 TreeNode(10, TreeNode(9), TreeNode(11)))
t = Solution()
a = t.Print(Tree1)
print(a)