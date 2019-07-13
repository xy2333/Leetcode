# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next_ = None):
        self.val = x
        self.next = next_

class Solution:
	def sortList(self, head):
		if head is None or head.next is None:
			return head
		fp = sp = head
		presp = None
		while fp is not None and fp.next is not None:
			fp = fp.next.next
			presp = sp
			sp = sp.next
		presp.next = None
		p1 = self.sortList(head)
		p2 = self.sortList(sp)
		if p1 is None:
			return p2
		if p2 is None:
			return p1
		phead = q = ListNode(0)

		while p1 is not None and p2 is not None:
			if p1.val <= p2.val:
				q.next = p1
				p1 = p1.next
			else:
				q.next = p2
				p2 = p2.next
			q = q.next
		if p1 is None:
			q.next = p2
		else:
			q.next = p1
		return phead.next