# -*- coding:utf-8 -*-


class GrayCode:
    def getGray(self, n):
        # write code here
        import math
        res = [0]*(n+1)
        m = math.ceil(math.log(n+1, 2))
        for i in range(int(m)):
            flag = True
            temp = 0
            # if 2**i < n+1:
            for j in range(2**i, n+1):
                temp += 1
                if temp > 2**(i+1):
                    flag = not flag
                    temp = 1
                if flag:
                    res[j] += 2**i
        for k in range(n+1):
        	res[k] = self.tran(res[k],m)
        return res

    def tran(self,num,m):
    	s = bin(num)[2:]
    	return '0'*(m-len(s))+s

# t = GrayCode()
# a = t.getGray(1)
# print(a)

class Gift:
	def getValue(self, gifts, n):
		# write code here
		if n == 0:
			return 0
		flag = 1
		gifts.sort()
		mid = gifts[n//2]
		end = n//2
		for i in range(n//2,n):
			if gifts[i] == mid:
				end += 1
			else:
				break
		start = n//2
		for i in range(n//2,-1,-1):
			if gifts[i] == mid:
				start -= 1
			else:
				break
		num = end - start - 1
		if num > n//2:
			return mid
		else:
			return 0


t = Gift()
a = t.getValue([1,2,3,3,3],5)
print(a)