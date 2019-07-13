class Solution:
	def wiggleSort(self, nums):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		if len(nums) <= 1:
			return
		n = len(nums)//2
		self.rec(nums,n,0,len(nums))
		for i in range(1,n,2):
			nums[i],nums[n+i] = nums[n+i],nums[i]
		# if nums[n] == nums[n-1]:
		# 	nums[n],nums[-1] = nums[-1],nums[n]
		# elif n+1 < len(nums) and nums[n] == nums[n+1]:
		# 	# nums[n],nums[0] = nums[0],nums[n]
		# 	r = nums[n]
		# 	nums[n:-1] = nums[n+1:]
		# 	nums[-1] = r
		# if nums[n] == nums[n-1] or (n+1 < len(nums) and nums[n] == nums[n+1]):
		# 	r = nums[n]
		# 	nums[n:-1] = nums[n+1:]
		# 	nums[-1] = r

		# if nums[n] == nums[n-1] and n//2 == 1:
		# 	nums[n],nums[-1] = nums[-1],nums[n]
		# elif (n+1 < len(nums) and nums[n] == nums[n+1]) and n//2 == 1:
		# 	nums[n],nums[0] = nums[0],nums[n]
		# elif nums[n] == nums[n-1] or (n+1 < len(nums) and nums[n] == nums[n+1]):
		# 	r = nums[n]
		# 	nums[n:-1] = nums[n+1:]
		# 	nums[-1] = r
		if nums[n] == nums[n-1]:
			nums[n],nums[-1] = nums[-1],nums[n]
		elif (n+1 < len(nums) and nums[n] == nums[n+1]) and nums[n] != nums[0]:
			nums[n],nums[0] = nums[0],nums[n]
		elif (n+1 < len(nums) and nums[n] == nums[n+1]) and nums[n] == nums[0]:
			r = nums[n]
			nums[n:-1] = nums[n+1:]
			nums[-1] = r
		return nums

	
	def rec(self,nums,n,begin,end):
		if begin+1 >= end:
			return
		mid = (begin+end)//2
		r = nums[begin]
		i = begin
		for j in range(begin+1,end):
			if nums[j] < r:
				i += 1
				nums[i],nums[j] = nums[j],nums[i]
		nums[begin],nums[i] = nums[i],nums[begin]
		if i == n:
			return 
		else:
			if i > n:
				self.rec(nums,n,begin,i)
			else:
				self.rec(nums,n,i+1,end)




lst = [1,5,1,1,6,4]
t = Solution()
print(t.wiggleSort(lst))
