# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next_ = None):
        self.val = x
        self.next = next_

class Solution:
	def mergeKLists(self, lists):
		if len(lists) == 0:
			return None
		if len(lists) == 1:
			return lists[0]
		return self.merge(self.mergeKLists(lists[:len(lists)//2]),self.mergeKLists(lists[len(lists)//2:]))
	def merge(self,lst1,lst2):
		if lst1 is None and lst2 is None:
			return None
		if lst1 is None:
			return lst2
		if lst2 is None:
			return lst1
		res = ListNode(0)
		phead = res
		while lst1 is not None and lst2 is not None:
			if lst1.val < lst2.val :
				res.next = lst1
				lst1 = lst1.next
			else:
				res.next = lst2
				lst2 = lst2.next
			res = res.next
		if lst1 is None:
			res.next = lst2
		else:
			res.next = lst1
		return phead.next      


a = ListNode(1, ListNode(3,ListNode(5)))
b = ListNode(2, ListNode(4,ListNode(6)))
s = [a,b]
t = Solution()
res = t.mergeKLists(s)
print(res)