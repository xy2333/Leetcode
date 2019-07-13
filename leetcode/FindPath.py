 # -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res = []

    def FindPath(self, root, expectNumber):
        # write code here
        path = []
        self.preorder(root, path, expectNumber)
        return self.res

    def preorder(self, root, path, expectNumber):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None and sum(path) == expectNumber:
            # 如果使用self.res.append(path)，那么res中的变量会随着path的变化而变化
            temp = list(path)
            self.res.append(temp)
        self.preorder(root.left, path, expectNumber)
        self.preorder(root.right, path, expectNumber)
        path.pop()


s = TreeNode(10, TreeNode(5, TreeNode(4), TreeNode(7)), TreeNode(12))
t = Solution()
a = t.FindPath(s, 15)
print(a)
