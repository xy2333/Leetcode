class Solution:
	def climbStairs(self, n):
		dp = [0]*(n+1)
		dp[0] = dp[1] = 1
		for i in range(2,n+1):
			dp[i] = dp[i-1]+dp[i-2]
		return dp[-1]
			pass



m = 3
n = 2
t = Solution()
print(t.uniquePaths(3,2))
