class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		tail = []
		for i in range(len(nums)):
			start = 0
			end = len(tail)
			temp = None
			while start < end:
				mid = (end+start)//2
				if tail[mid] >= nums[i] and (mid-1 < 0 or tail[mid-1] < nums[i]):
					temp = mid
					tail[mid] = nums[i]
					break
				else:
					if tail[mid] < nums[i]:
						start = mid+1
					else:
						end = mid
			if temp is None:
				tail.append(nums[i])
		return len(tail)