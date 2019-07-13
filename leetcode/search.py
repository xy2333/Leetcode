class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if len(nums) == 0:
			return -1
		index = self.findstart(nums)
		if target == nums[0]:
			return 0
		elif target > nums[0]:
			res = self.findtarget(nums[:index],target)
			if res is None:
				return -1
			else:
				return res
		else:
			res = self.findtarget(nums[index:],target)
			if res is None:
				return -1
			else:
				return index+res


	def findstart(self,nums):
		def rec(nums,begin,end):
			if end-begin < 1:
				return begin
			mid = (begin+end)//2
			if mid-1 >= begin and nums[mid-1] > nums[mid]:
				return mid
			else:
				if nums[mid] < nums[0]:
					return rec(nums,begin,mid)
				else:
					return rec(nums,mid+1,end)
		return rec(nums,0,len(nums))

	def findtarget(self,lst,target):
		def rec(lst,begin,end,target):
			if end-begin < 1:
				return None
			mid = (begin+end)//2
			if lst[mid] == target:
				return mid
			elif lst[mid] > target:
				return rec(lst,begin,mid,target)
			else:
				return rec(lst,mid+1,end,target)

		return rec(lst,0,len(lst),target)


t = Solution()
nums = [4,5,6,7,0,1,2]

res = t.search(nums,0)
print(res)

