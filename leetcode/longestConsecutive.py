class Solution:
	def longestConsecutive(self, nums):
		if len(nums) == 0:
			return 0
		d = set(nums)
		maxnum = 1
		for i in d:
			if i-1 not in d:
				num = 1
				temp = i
				while temp+1 in d:
					temp += 1
					num += 1
				maxnum = max(maxnum,num)
		return maxnum

        

        

        
s = [100,4,200,1,3,2]
t = Solution()
print(t.longestConsecutive(s))