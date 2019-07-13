class Solution:
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

		def dp(nums,dplist):
			a = []
			for j in letter[nums]:
				a = a+[k+j for k in dplist]
			return a

		if len(digits) == 0:
			return []
		
		dplist = [x for x in letter[digits[0]]]

		if len(digits) > 1:
			for i in range(1,len(digits)):
				dplist = dp(digits[i],dplist)

		return dplist

s = ''
t = Solution()
a=t.letterCombinations(s)
print(a)