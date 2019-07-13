# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
	    def isInterger(m):
	    	if len(m) <= 0:
	    		return False
	    	if m[0] in '+-':
	    		m = m[1:]
	    	return isUnsignedInterger(m)

	    def isUnsignedInterger(m):
	    	if len(m) <= 0:
	    		return False
	    	for i in range(len(m)):
	    		if m[i] not in '0123456789':
	    			return False
	    	return True

	    s = s.lower()
	    if '.' in s:
	    	index = s.index('.')
	    	result = isInterger(s[:index]) or not s[:index] or s[:index] == '-' or s[:index] == '+'
	    	if 'e' in s[index+1:]:
	    		index2 = s.index('e')
	    		result = result and isInterger(s[index2+1:]) and isUnsignedInterger(s[index+1:index2])
	    	else:
	    		result = result and isUnsignedInterger(s[index+1:])
	    elif 'e' in s:
	    	index2 = s.index('e')
	    	result = isInterger(s[:index2]) and isInterger(s[index2+1:])
	    else:
	    	result = isInterger(s)
	    return result

t = Solution()
s = '-.123'
a = t.isNumeric(s)
print(a)