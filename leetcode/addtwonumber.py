# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class LinkList(object):
#     def __init__(self):
#         self.head = None

#     #链表初始化函数, 方法类似于尾插
#     def initList(self, data):
#         #创建头结点
#         self.head = ListNode(data[0])
#         p = self.head
#         #逐个为 data 内的数据创建结点, 建立链表
#         for i in data[1:]:
#             node = ListNode(i)
#             p.next = node
#             p = p.next

# class Solution:
# 	def addTwoNumbers(self, l1, l2):
# 		len1 = len(l1)
# 		len2 = len(l2)
# 		if len1 > len2:
# 			lensum = len1
# 			for i in range(len1-len2):
# 				l2 = l2+[0]
# 		else:
# 			lensum = len2
# 			for i in range(len2-len1):
# 				l1 = l1+[0]

# 		carry = 0
# 		sums = [0]*lensum
# 		ans = [0]*lensum
# 		for j in range(lensum):
# 			sums[j] = l1[j]+l2[j]+carry
# 			carry = sums[j]//10
# 			ans[j] = sums[j]%10
# 		if carry == 1:
# 			ans = ans+[1]
# 		return ans

        
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str_l1, str_l2 = '', ''
        while l1:            
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2:            
            str_l2 += str(l2.val)
            l2 = l2.next
        int_l1 = int(str_l1[::-1])
        int_l2 = int(str_l2[::-1])       
        return list(map(int, str(int_l1 + int_l2)[::-1]))


# l2 = [1,3,5]
# l1 = [4,5,7,8,1]
# s = Solution()
# a=s.addTwoNumbers(l1,l2)
# print(a)
