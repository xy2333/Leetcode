class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        

s = "hello"
s2 = "ll"
t = Solution()
a=t.strStr(s,s2)
print(a)