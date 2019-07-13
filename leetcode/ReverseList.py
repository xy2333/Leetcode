# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        if pHead.next is None:
            return pHead
        re = None
        while pHead is not None:
            i = pHead
            pHead = pHead.next
            i.next = re
            re = i
        return re

    def printall(self, head_node):
        if head_node is None:
            return
        while head_node is not None:
            print(head_node.val)
            head_node = head_node.next


t = Solution()
s = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
t.printall(s)
print('*********************************************')
a = t.ReverseList(s)
t.printall(a)
