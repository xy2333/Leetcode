class Solution:
	def subsets(self, nums):
		res = [[]]
		for i in nums:
			res += [x+[i] for x in res]
		return res


t = Solution()
nums = [1,2,3]
print(t.subsets(nums))