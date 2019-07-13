# # def question1(num):
# # 	if not num:
# # 		return
# # 	res = []
# # 	for strs in num:
# # 		length = len(num)
# # 		if length <= 1:
# # 			res.append(0)
# # 		i = 0
# # 		j = length-1


# # 			pass

# # 		pass

# # def remax(strs):
# # 	i = 0
# # 	j = length-1
# # 	pass

# # def question2(strs):
# # 	if strs == '':
# # 		return ''
# # 	lst = list(strs)
# # 	i = j = 0
# # 	while j < len(lst):
# # 		if ord(lst[j]) >= 97:
# # 			temp = lst[j]
# # 			lst[i+1:j+1] = lst[i:j]
# # 			lst[i] = temp
# # 			i += 1
# # 			j += 1
# # 		else:
# # 			j += 1
# # 	return ''.join(lst)

# # def question3(num,N):
# # 	if N == 1:
# # 		return [0,0]
# # 	nmax = nmin = 1
# # 	dmax = abs(num[0]-num[1])
# # 	dmin = abs(num[0]-num[1])

# # 	for i in range(len(num)):
# # 		for j in range(i+1,len(num)):
# # 			temp = abs(num[j]-num[i])
# # 			if temp > dmax:
# # 				nmax = 1
# # 				dmax = temp
# # 			elif temp == dmax:
# # 				nmax += 1
# # 			if temp < dmin:
# # 				nmin = 1
# # 				dmin = temp
# # 			elif temp == dmin:
# # 				nmin += 1
# # 	return [nmin,nmax]

# def question3(num,N):
# 	if N == 1:
# 		return [0,0]
# 	num.sort()
# 	if num[0] == num[-1]:
# 		return [N*(N-1)/2,N*(N-1)/2]
# 	else:
# 		nmax = num.count(num[0])*num.count(num[-1])
# 		dict_num = {}
# 		for i in num:
# 			if i in dict_num:
# 				dict_num[i] += 1
# 			else:
# 				dict_num[i] = 1

# 		if len(dict_num) != N:
# 			nmin = 0
# 			for i in dict_num:
# 				nmin += dict_num[i]*(dict_num[i]-1)/2
# 		else:
# 			diff = []
# 			for i in range(N-1):
# 				diff.append(abs(num[i],num[i+1]))
# 			diff.sort()
# 			nmin = diff.count(diff[0])
# 	return [int(nmin),int(nmax)]

# s = [45,12,45,32,5,6]
# a = question3(s,6)
# print(a)

# while 1:
#     try:
#         N = input()
#         s = input()
#         num = [int(i) for i in list(s.split(' '))]
#     except:
#         break
#     a = question3(num,N)
#     print(str(a[0])+' '+str(a[1]))


# import sys

# def question3(line,N):
# 	if N == 1:
# 		return [0,0]
# 	num = list(map(int, line.strip().split()))
# 	num.sort()
# 	if num[0] == num[-1]:
# 		return [N*(N-1)/2,N*(N-1)/2]
# 	else:
# 		nmax = num.count(num[0])*num.count(num[-1])
# 		dict_num = {}
# 		for i in num:
# 			if i in dict_num:
# 				dict_num[i] += 1
# 			else:
# 				dict_num[i] = 1

# 		if len(dict_num) != N:
# 			nmin = 0
# 			for i in dict_num:
# 				nmin += dict_num[i]*(dict_num[i]-1)/2
# 		else:
# 			diff = []
# 			for i in range(N-1):
# 				diff.append(abs(num[i],num[i+1]))
# 			diff.sort()
# 			nmin = diff.count(diff[0])
# 	return [int(nmin),int(nmax)]

# j = 0
# for line in sys.stdin:
#     j += 1
#     if j % 2 == 1:
#         length = int(line.strip())
#     else:
#         a = question3(line, length)
#         print(str(a[0])+' '+str(a[1]))


# import sys
# k = 0
# for line in sys.stdin:
#     k = 1 - k
#     if (k == 0): 
#         nums = [int(i) for i in line.strip().split()]
#         m = len(nums)  
#         a = question3(nums,m)
#         print(str(a[0])+' '+str(a[1]))

class Solution():
	"""docstring for Solution"""
	def __init__(self):
		self.s1 = None
		self.s2 = None
		self.max_mat = [[],[]]

		
	def question1(self,strs):
		length = len(strs)
		re_strs = strs[::-1]
		self.s1 = strs
		self.s2 = re_strs
		self.max_mat[0] = [0]*length
		for j in range(length):
			for i in range(length):
				longest = self.maxsum(i,j)
				self.max_mat[1].append(longest)
			self.max_mat[0] = self.max_mat[1]
			self.max_mat[1] = []
		return length-self.max_mat[0][-1]


	def maxsum(self,i,j):
		if self.s1[i] == self.s2[j]:
			if i > 0:
				return 1+self.max_mat[0][i-1]
			else:
				return 1
		else:
			if i > 0:
				return max(self.max_mat[1][i-1],self.max_mat[0][i])
			else:
				return self.max_mat[0][i]

t = Solution()
s = 'hlcdrakpjavajohvajymzrwrdnwjboedcxqbuyevoxsyhymwtixlddytqfavtxzkeirzxsrrdzummbrbrjzxriufuafuabvumiratbbvxgxjvjauovcmqjuduuzmgveratjhwgsllnblfeibwyzimcbvoquvsluvlogtbisfzutqrrhlgufgqcemzbcfpvclogoqqhkmlvwqwtyegquglmhiunkmyocpddtkynkryiwxqrbyxnwajuxtqgqvknlhjuzxjckbwmgnizxxgtkblycvabgpuqeamlalyrwgiikixhuosctwrnybknwgdoecdlziwzmadbuemgygunxyosvurdmqawiuibmcznaeyritmlqjrmvnemcajeqijeyaufhvogsaikmtefitqpjfcajhfcqctvloiqyjvshoqbvjrdxajsdqvqpcxfqaekibtxvrxyxxydhwafllduxmtosnukxkcpthqlcyutghhltqntvntspecvhgbitlwklsomtbryrzxvolfmznicnstauwgdcateuxoueuzpzdzdauebtgboyqsllhnggxfgmfiaznjhrddrdliurxvckmolzfpebcpjvvhhfnassiidfiumnhzxshczvlchjxtvevgnajsmsihpuaxbmxvbvdbtloleidptbfkpjgslfzuuvlxaemscbgqlmwbwlaimttkutmwkcsodbxxauuudqeqkyddzrohulndqslhflhvjufnnwjgtm'
a = t.question1(s)
print(a)

# 可以全部通过的代码
import sys
while True:
    s = sys.stdin.readline().strip()
    s_reverse = s[::-1]
    if len(s) == 0:
        break
    else:
        c = [[0 for col in range(len(s)+1)] for row in range(len(s_reverse)+1)]
        for i in range(len(s)):
            for j in range(len(s_reverse)):
                if s[i] == s_reverse[j]:
                    c[i+1][j+1] = c[i][j] + 1
                else:
                    c[i+1][j+1] = max(c[i+1][j],c[i][j+1])
        print len(s)-c[-1][-1]