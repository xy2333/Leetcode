class Solution:
	def reverseWords(self, s):
		return ' '.join(s.split()[::-1])[::-1]





s = "Let's take LeetCode contest"
t = Solution()
print(t.reverseWords(s))
