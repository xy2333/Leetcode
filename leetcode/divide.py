class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend >= 0 and divisor > 0:
        	flag = 0
        elif dividend <=0 and divisor <0:
        	flag = 0
        else:
        	flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        i = 1
        res = 0
        temp = divisor
        while dividend >= divisor:
        	if dividend >= temp:
        		dividend = dividend - temp
        		res += i
        		i <<= 1
        		temp <<= 1
        	else:
        		i >>= 1
        		temp >>= 1


        if flag == 1:
        	res = -res
        return min(max(res,-2147483648),2147483647)

s = 10
s2 = 3
t = Solution()
a=t.divide(s,s2)
print(a)