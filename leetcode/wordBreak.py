class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		d = set(wordDict)
		dp = [False]*(len(s)+1)
		dp[0] = True
		for i in range(1,len(s)+1):
			for j in range(i):
				dp[i] = dp[j] and (s[j:i] in d)
				if dp[i]:
					break
		return dp[-1]

s = "leetcode"
d = ["leet", "code"]
t = Solution()
print(t.wordBreak(s,d))