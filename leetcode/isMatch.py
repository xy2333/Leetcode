import time

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
        	if len(s) == 0:
        		return bool(1)
        	else:
        		return bool(0)
        first_match = bool(s) and p[0] in {s[0],'.'}
        if len(p) >= 2 and p[1] == '*':
        	return self.isMatch(s,p[2:]) or (first_match and self.isMatch(s[1:],p))
       	else:
        	return first_match and self.isMatch(s[1:],p[1:])

# DP

# class Solution(object):
#     def isMatch(self, text, pattern):
#         memo = {}
#         def dp(i, j):
#             if (i, j) not in memo:
#                 if j == len(pattern):
#                     ans = i == len(text)
#                 else:
#                     first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                     if j+1 < len(pattern) and pattern[j+1] == '*':
#                         ans = dp(i, j+2) or first_match and dp(i+1, j)
#                     else:
#                         ans = first_match and dp(i+1, j+1)

#                 memo[i, j] = ans
#             return memo[i, j]

#         return dp(0, 0)







# start = time.perf_counter()
s = 'aaaaaaaaaaaaab'
p = 'a*a*a*a*a*a*a*a*a*a*b'
t = Solution()
a=t.isMatch(s,p)
print(a)
# end = time.perf_counter()
# print('final is in ',end-start)

     