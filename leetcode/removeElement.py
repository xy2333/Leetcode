class Solution:
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		i = 0
		while i < len(nums):
			if nums[i] == val:
				nums.pop(i)
			else:
				i = i+1
		return len(nums)





s = [0,1,2,2,3,0,4,2]
t = Solution()
a=t.removeElement(s,2)
print(a)