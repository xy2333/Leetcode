class Solution():
	"""docstring for Solution"""
	def question1(self,num):
		lens = num[0]
		if num[0] == 0:
			return 0
		res = []
		for i in range(lens):
			a = b = 0
			flag = 0
			a += num[1+i]
			flag = 1
			newl = num[i+2:]+num[1:i+1]
			while len(newl) >= 2:
				if flag == 1:
					if newl[0] >= newl[-1]:
						index = 0
					else:
						index = -1
					b += newl[index]
					flag = 0
					newl.pop(index)
				else:
					if newl[0] >= newl[-1]:
						index = 0
					else:
						index = -1
					a += newl[index]
					flag = 1
					newl.pop(index)
			if len(newl) == 0:
				res.append(abs(a-b))
			else:
				if flag == 0:
					a += newl[0]
				else:
					b += newl[0]
				res.append(abs(a-b))
		return min(res)

	def question2(self,num,N):
		if N == 0:
			return
		un_repair = set(num)
		i = 0
		minlength = N
		res = []
		while i < N-len(un_repair)+1:
			lst = set()
			j = i
			while j < N:
				lst.add(num[j])
				if len(lst) != len(un_repair):
					j += 1
				else:
					length = j+1-i
					if length < minlength:
						res = []
						res.append([i+1,j+1])
						minlength = length
					elif length == minlength:
						res.append([i+1,j+1])
					break
			i += 1
		return minlength,res

	def question22(self,num,N):
		if N == 0:
			return
		un_repair = set(num)
		i = 0
		j = 0
		minlength = N
		res = []
		while j <= N:
			if len(set(num[i:j])) != len(un_repair):
				j += 1
			else:
				length = j-i
				if length < minlength:
					res = []
					res.append([i+1,j])
					minlength = length
				elif length == minlength:
					res.append([i+1,j])
				i += 1
		return minlength,res

	def question222(self,num,N):
		if N == 0:
			return
		un_repair = set(num)
		i = 0
		j = 0
		lst = set()
		dict_num = {}
		while len(lst) != len(un_repair):
			if num[j] in dict_num:
				dict_num[num[j]] += 1
			else:
				dict_num[num[j]] = 1
			lst.add(num[j])
			j += 1

		minlength = N
		res = []
		length = j-i
		if length < minlength:
			res = []
			res.append([i+1,j])
			minlength = length
		elif length == minlength:
			res.append([i+1,j])
		
		while 1: 		
			delete = num[i]
			dict_num[num[i]] -= 1
			i += 1
			if dict_num[delete] != 0:
				length = j-i
				if length < minlength:
					res = []
					res.append([i+1,j])
					minlength = length
				elif length == minlength:
					res.append([i+1,j])
			else:
				while j < N:
					if num[j] == delete:
						dict_num[delete] += 1
						j += 1
						length = j-i
						if length < minlength:
							res = []
							res.append([i+1,j])
							minlength = length
						elif length == minlength:
							res.append([i+1,j])
						break
					else:
						dict_num[num[j]] += 1
						j += 1
				if j >= N:
					if dict_num[delete] == 0:
						break

		return minlength,res

# t = Solution()
# N = int(input())
# s = []
# for i in range(N):
#     s.append(int(input()))
# a = t.question22(s,N)
# print(a[0],len(a[1]))
# for i in a[1]:
#     print(str(i).replace(' ',''),end = ' ')

s = [1,1,3,4,6,6,5,1,3,3]
t = Solution()		
a = t.question222(s,10)
print(a[0],len(a[1]))
for i in a[1]:
    print(str(i).replace(' ',''),end = ' ')