class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		fp = nums[nums[0]]
		sp = nums[0]
		while sp != fp:
			fp = nums[nums[fp]]
			sp = nums[sp]
		step = 1
		p = nums[fp]
		while p != sp:
			p = nums[p]
			step += 1
		p = nums[0]
		q = nums[0]
		for i in range(step):
			p = nums[p]
		while p != q:
			p = nums[p]
			q = nums[q]
		return q


t = Solution()
s = [1,3,4,2,2]

res = t.findDuplicate(s)
print(res)