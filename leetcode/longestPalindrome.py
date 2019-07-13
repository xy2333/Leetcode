import numpy
class Solution:
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if len(s) == 0:
			return ''

		res = ''
		for i in numpy.arange(0,len(s)-0.5,0.5):
			if i%1 == 0:
				i = int(i)
				resi = s[i]
				for j in range(len(s)+1):
					if (i-j) >=0 and (i+1+j) <= (len(s)-1):
						if s[i-j:i+1+j] == s[i-j:i+1+j][::-1]:
							resi = s[i-j:i+1+j]
						else:
							if len(resi) > len(res):
								res = resi
							break
					elif (i-j) >=0 and (i+1+j) == len(s):
						if s[i-j:] == s[i-j:][::-1]:
							resi = s[i-j:]
						else:
							if len(resi) > len(res):
								res = resi
							break
					else:
						if len(resi) > len(res):
							res = resi
						break
			else:
				i = int(i)
				if s[i] == s[i+1]:
					resi = s[i:i+2]
					for j in range(len(s)+1):
						if (i-j) >=0 and (i+2+j) <= (len(s)-1):
							if s[i-j:i+2+j] == s[i-j:i+2+j][::-1]:
								resi = s[i-j:i+2+j]
							else:
								if len(resi) > len(res):
									res = resi
								break
						elif (i-j) >=0 and (i+2+j) == len(s):
							if s[i-j:] == s[i-j:][::-1]:
								resi = s[i-j:]
							else:
								if len(resi) > len(res):
									res = resi
								break
						else:
							if len(resi) > len(res):
								res = resi
							break
		return res

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         n = len(s)
#         maxl = 0
#         start = 0
#         for i in range(n):
#             if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
#                 start = i - maxl - 1
#                 maxl += 2
#                 continue
#             if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
#                 start = i - maxl
#                 maxl += 1
#         return s[start: start + maxl]

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         start = 0
#         end = 0
#         maxlength = 0
#         n = len(s)
#         for i in range(2*n-1):
#             if i%2 == 0:
#                 temp_start = int(i/2)
#                 temp_end = temp_start+1
#                 length = 0
#                 temp_s = s[temp_start:temp_end]
#                 while temp_s == temp_s[::-1]:
#                     length = temp_end - temp_start
#                     temp_start-=1
#                     temp_end+=1
#                     if temp_start < 0 or temp_end >n:
#                         length = temp_end - temp_start - 2
#                         temp_start+=1
#                         temp_end-=1
#                         break
#                     else:
#                         temp_s = s[temp_start:temp_end]
#                 if length >= maxlength:
#                     maxlength,start,end = length,temp_start,temp_end
#             else:
#                 temp_start = int(i/2)
#                 temp_end = temp_start+2
#                 length = 0
#                 temp_s = s[temp_start:temp_end]
#                 while temp_s == temp_s[::-1]:
#                     length = temp_end - temp_start
#                     temp_start-=1
#                     temp_end+=1
#                     if temp_start < 0 or temp_end >n:
#                         length = temp_end - temp_start - 2
#                         temp_start+=1
#                         temp_end-=1
#                         break
#                     else:
#                         temp_s = s[temp_start:temp_end]
#                 if length >= maxlength:
#                     maxlength,start,end = length,temp_start,temp_end
#         return s[start:end]



s = "cbbd"
t = Solution()
a=t.longestPalindrome(s)
print(a)
