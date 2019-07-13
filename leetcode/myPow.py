class Solution:
	def myPow(self, x, n):
		# if n == 0:
		# 	return 1
		# if n > 0 :
		# 	flag = 1
		# else:
		# 	flag = 0
		# 	n = -n

		# if n%2 == 0:
		# 	return (self.myPow(x,n/2))**(2*(-1)**(flag+1))
		# else:
		# 	return (self.myPow(x,n//2))**(2*(-1)**(flag+1))*(x**((-1)**(flag+1)))
		if n < 0:
		    x = 1/x
		    n = -n
		    
		if n == 0:
		    return 1
		if n == 1:
		    return x

		if n % 2 == 0:
		    return self.myPow(x, n/2)**2
		else:
		    return self.myPow(x, n-1) * x

        



coins = [2]
amount = 11
t = Solution()
print(t.myPow(2,-2147483648))
