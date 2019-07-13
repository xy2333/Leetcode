class Solution:
    def generateMatrix(self, n):
    	res = [[n*n]]
    	i = n*n
    	while i > 1:
    		res = self.rotate(res)
    		res.insert(0, list(range(i-len(res[0]),i)))
    		i -= len(res[0])
    	return res



    def rotate(self,lst):
    	res = []
    	for i in range(len(lst[0])):
    		res.append([j[i] for j in lst[::-1]])
    	return res