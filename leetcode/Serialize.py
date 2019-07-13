# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sTree = ''

    def Serialize(self, root):
        # write code here
        self.preorder(root)
        return self.sTree[:-1]

    def preorder(self, root):
        if root is None:
            self.sTree += '$,'
            return
        self.sTree += str(root.val) + ','
        self.preorder(root.left)
        self.preorder(root.right)

    def Deserialize(self, s):
        # write code here
        s = s.split(',')
        return self.rec(s)

    def rec(self, s):
        if s is None:
            return
        if s[0] is '$':
            s.pop(0)
            return
        pRoot = TreeNode(int(s[0]))
    # 在子函数中新的s 不同于上一层函数中的s
        s.pop(0)
        pRoot.left = self.rec(s)
        pRoot.right = self.rec(s)
        return pRoot
# class Solution:
#     def Serialize(self, root):
#         # write code here
#         if root == None:
#             return "#"
#         return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)

#     def Deserialize(self, s):
#         # write code here
#         root, index = self.deserialize(s.split(","), 0)
#         return root

#     def deserialize(self, s, index):
#         if s[index] == "#":
#             return None, index + 1
#         root = TreeNode(int(s[index]))
#         index += 1
#         root.left, index = self.deserialize(s, index)
#         root.right, index = self.deserialize(s, index)
#         return root, index

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
        return res



s = TreeNode(10, TreeNode(6, TreeNode(4), TreeNode(8)),
             TreeNode(14, TreeNode(12), TreeNode(16)))
t = Solution()
a = t.Serialize(s)
print(a)
b = t.Deserialize(a)
print(t.Print(b))
