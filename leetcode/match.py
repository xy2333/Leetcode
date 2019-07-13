# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
       	if len(s) == 0 and len(pattern) == 0:
       		return True
       	if len(s) != 0 and len(pattern) == 0:
       		return False
       	if len(pattern) >= 2 and pattern[1] == '*':
       		if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
       			return self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)
       		else:
       			return self.match(s,pattern[2:])
       	if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
       		return self.match(s[1:],pattern[1:])
       	return False


t = Solution()
s = 'abbc'
pattern = 'ab*c'
print(t.match(s,pattern))