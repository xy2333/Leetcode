# class Solution:
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if len(nums)<3:
#         	return target
#         sumclose = nums[0]+nums[1]+nums[2]
#         for i in itertools.combinations(nums,3):
#         	sums = i[0]+i[1]+i[2]
#         	if sums == target:
#         		return sums
#         	if abs(sums-target) < abs(sumclose-target):
#         		sumclose = sums
#         return sumclose


class Solution:
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums.sort()
		sumsclose = nums[0]+nums[1]+nums[2]
		for i in range(len(nums)-2):
			j = i+1
			k = len(nums)-1
			while j < k:
				sums = nums[i]+nums[j]+nums[k]
				if sums == target:
					return sums
				if abs(sums-target) < abs(sumsclose-target):
					sumsclose = sums
				if sums < target:
					j += 1
				else:
					k -= 1
		return sumsclose


import itertools
s = [-1,2,1,-4]
target = 1
t = Solution()
a=t.threeSumClosest(s,target)
print(a)
