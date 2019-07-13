class Solution:
    def grayCode(self, n):
    	if n == 0:
    		return [0]
    	if n == 1:
    		return [0,1]
    	res = [0,1]
    	for i in range(2,n+1):
    		res = res+[x+2**(i-1) for x in res[::-1]]
    	return res

        





s = 3
t = Solution()
print(t.grayCode(s))