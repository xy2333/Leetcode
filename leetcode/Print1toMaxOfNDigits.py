# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x,next_ = None):
        self.val = x
        self.next = next_
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        result = ListNode(0)
        res = result
        p = pHead
        while p is not None and p.next is not None:
            if p.val == p.next.val:
                while p.next is not None and p.val == p.next.val:
                    p = p.next
                p = p.next
            else:
                res.next = p
                res = res.next
                p = p.next
        res.next = p

        return result.next

    def printall(self,p):
        while p is not None:
            print(p.val)
            p = p.next

t = Solution()
s = ListNode(1,ListNode(2,ListNode(3, ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
a = t.deleteDuplication(s)
t.printall(a)


