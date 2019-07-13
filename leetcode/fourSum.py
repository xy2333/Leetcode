class Solution:	
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		def threeSum(nums,target):
			# if len(nums) < 3:
			# 	return []
			# for k in range(len(nums)-1,0,-1):
			# 	if nums.count(nums[k]) > 3:
			# 		nums.pop(k)
			# nums.sort()
			res = set()
			for i,v in enumerate(nums[:-2]):
				d = set()
				for j in nums[i+1:]:
					if j not in d:
						d.add(target-(j+v))
					else:
						res.add((v,j,target-(v+j)))
			return list(res)  
		
		if len(nums) < 4:
			return []
		for g in range(len(nums)-1,0,-1):
			if nums.count(nums[g]) > 4:
				nums.pop(g)
		nums.sort()
		res = set()
		countlist = []
		for i,v in enumerate(nums[:-3]):
			dplist = threeSum(nums[i+1:],target-v)
			if dplist != []:
				for p in dplist:
					countlist.append(list(p)+[v])
		for q in countlist:
			res.add(tuple(q))

		return list(res)

s = [1, 0, -1, 0, -2, 2]
target = 0
t = Solution()
a=t.fourSum(s,target)
print(a)