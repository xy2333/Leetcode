class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        intnum = 0
        i = len(s)-1
        while i >= 0:
        	if s[i] == 'I':
        		intnum = intnum+1
        		i = i-1
        	elif s[i] == 'V':
        		if i > 0 and s[i-1] == 'I':
        			intnum = intnum+4
        			i = i-2
        		else:
        			intnum = intnum+5
        			i = i-1
        	elif s[i] == 'X':
        		if i > 0 and s[i-1] == 'I':
        			intnum = intnum+9
        			i = i-2
        		else:
        			intnum = intnum+10
        			i = i-1        	
        	elif s[i] == 'L':
        		if i > 0 and s[i-1] == 'X':
        			intnum = intnum+40
        			i = i-2
        		else:
        			intnum = intnum+50
        			i = i-1
        	elif s[i] == 'C':
        		if i > 0 and s[i-1] == 'X':
        			intnum = intnum+90
        			i = i-2
        		else:
        			intnum = intnum+100
        			i = i-1
        	elif s[i] == 'D':
        		if i > 0 and s[i-1] == 'C':
        			intnum = intnum+400
        			i = i-2
        		else:
        			intnum = intnum+500
        			i = i-1
        	elif s[i] == 'M':
        		if i > 0 and s[i-1] == 'C':
        			intnum = intnum+900
        			i = i-2
        		else:
        			intnum = intnum+1000
        			i = i-1
        return intnum


class Solution:

	def romanToInt(self, s):
	    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	    z = 0
	    for i in range(0, len(s) - 1):
	        if roman[s[i]] < roman[s[i+1]]:
	            z -= roman[s[i]]
	        else:
	            z += roman[s[i]]
	    return z + roman[s[-1]]




s = 'MCMXCIV'
t = Solution()
a=t.romanToInt(s)
print(a)
