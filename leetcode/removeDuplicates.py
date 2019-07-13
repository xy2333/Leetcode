class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 1:
			return 1
		j = 0
		for i in range(len(nums)):
			# for j in range(i,len(nums)):
			# j = i
			while j < len(nums):
				if nums[i] == nums[j]:
					j = j+1
					if j == len(nums):
						return i+1					
				else:
					nums[i + 1] = nums[j]
					j = j+1
					if j == len(nums):
						return i+2
					break



s = [0,0,1,1,1,2,2,3,3,4]
# s = [1,1,2]
# s = [1,1]
t = Solution()
a=t.removeDuplicates(s)
print(a)