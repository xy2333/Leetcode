class Solution(object):
    def Add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        if b == 0:
            return a
        while b != 0:
            n1 = a^b
            n2 = (a&b)<<1
            a = n1&0xFFFFFFFF
            b = n2&0xFFFFFFFF
        return a if a>>31 == 0 else a-2**32    
        

t = Solution()
a = t.Add(1,-1)
print(a)