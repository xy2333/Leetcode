# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        tmp_carry = 0 
        tmp_sol = None
        head_sol = None

        while l1 != None or l2 != None or tmp_carry>0:
            tmp_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + tmp_carry
            tmp_carry = (tmp_sum - tmp_sum%10)/10
            if tmp_sol:
                tmp_sol.next = ListNode(tmp_sum%10)
                tmp_sol = tmp_sol.next
            else:
                tmp_sol = ListNode(tmp_sum%10)
                head_sol = tmp_sol
            l1 = l1.next if l1!=None else None
            l2 = l2.next if l2!=None else None
        return head_sol

l2 = [1,3,5]
l1 = [4,5,7,8,1]
s = Solution()
a=s.addTwoNumbers(l1,l2)
print(a)