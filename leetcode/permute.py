class Solution:
	def permute(self, nums):
		res = [[]]			
		for i in nums:
			temp = []
			length = len(res[0])
			for lst in res:
				for j in range(length+1):
					lst.insert(j,i)
					temp.append(list(lst))
					lst.pop(j)
			res = temp
		return res



nums = [1,2,3]
t = Solution()
print(t.permute(nums))