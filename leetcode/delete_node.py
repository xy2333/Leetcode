class ListNode:
    def __init__(self,val,next_ = None):
        self.val = val
        self.next = next_

class Solution:
	def deleteDuplication(self, pHead):
		# write code here
		result = ListNode(0,pHead)
		temp = result
		while temp.next is not None and temp.next.next is not None:
			if temp.next.val == temp.next.next.val:
				samelist = temp.next.next
				while samelist.next is not None and samelist.next.val == samelist.val:
					samelist = samelist.next
				temp.next = samelist.next
			else:
				temp = temp.next  
		return result.next

	def delete_node(self,head_node,del_node):
		"""
		删除指定节点
		"""
		if del_node.next is None:
			if head_node == del_node:
				head_node.val = None
				head_node.next = None
			else:
				while head_node.next is not del_node:
					head_node = head_node.next
				head_node.next = None
		else:
			del_node.val = del_node.next.val
			del_node.next = del_node.next.next

	def printall(self,head_node):
		if head_node is None:
			return
		while head_node is not None:
			print(head_node.val)
			head_node = head_node.next

# c = ListNode(3)
# b = ListNode(2, c)
# a = ListNode(1,b)
t = Solution()
# t.printall(a)
# print('****************************')
# t.delete_node(a,c)
# t.printall(a)
# print('****************************')
# m = ListNode(1)
# t.printall(m)
# print('****************************')
# t.delete_node(m,m)
# t.printall(m)

m = ListNode(1,ListNode(2,ListNode(3, ListNode(3, ListNode(4)))))
t.printall(m)
print('****************************')
t.printall(t.deleteDuplication(m))

print('****************************')
m = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(4)))))
t.printall(m)
print('****************************')
t.printall(t.deleteDuplication(m))

print('****************************')
m = ListNode(1,ListNode(1,ListNode(3, ListNode(4, ListNode(4)))))
t.printall(m)
print('****************************')
t.printall(t.deleteDuplication(m))

print('****************************')
m = ListNode(1,ListNode(1,ListNode(1, ListNode(1, ListNode(1)))))
t.printall(m)
print('****************************')
t.printall(t.deleteDuplication(m))

# print('****************************')
# m = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
# t.printall(m)
# print('****************************')
# t.deleteDuplication(m)
# t.printall(m)
# print('****************************')
# m = None
# t.printall(m)
# print('****************************')
# t.deleteDuplication(m)
# t.printall(m)
print('****************************')
m = ListNode(1,ListNode(2,ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
t.printall(m)
print('****************************')
t.printall(t.deleteDuplication(m))