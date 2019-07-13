# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None and pHead2 is None:
        	return None
        if pHead1 is None:
        	return pHead2
        if pHead2 is None:
        	return pHead1
        if pHead1.val <= pHead2.val:
        	m = pHead1
        	pHead1 = pHead1.next
        	m.next = self.Merge(pHead1,pHead2)
        	return m
        else:
        	m = pHead2
        	pHead2 = pHead2.next
        	m.next = self.Merge(pHead1,pHead2)
        	return m


    def printall(self, head_node):
        if head_node is None:
            return
        while head_node is not None:
            print(head_node.val)
            head_node = head_node.next


t = Solution()
s1 = ListNode(1, ListNode(3, ListNode(5)))
t.printall(s1)
print('********************************')
s2 = ListNode(2, ListNode(4, ListNode(6)))
t.printall(s2)
print('********************************')
a = t.Merge(s1,s2)
t.printall(a)
