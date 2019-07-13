class Solution:
    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
    #     s = str(x)
    #     return bool(s == s[::-1])
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            x_right = 0
            while x > x_right:
                x_right = x_right * 10 + x % 10
                x = x // 10
        return x == x_right or x == x_right // 10


intnum = 11
t = Solution()
a = t.isPalindrome(intnum)
print(a)
