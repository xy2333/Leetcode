# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) == 0:
        	return
        columns = len(matrix)
        rows = len(matrix[0])
        i = 0
        j = 0
        lmatrix = []
        while i < rows/2 and j < columns/2:
        	lmatrix += self.printcircle(i,j,matrix)
        	i += 1
        	j += 1
        return lmatrix

    def printcircle(self,i,j,matrix):
    	startrow = i
    	startcolumns = j
    	result = []
    	for j in range(startcolumns,len(matrix)-j):
    		result.append(matrix[j][i])
    	if len(matrix[0])-2*startrow <= 1:
    		return result
    	else:
    		for i in range(startrow+1,len(matrix[0])-startrow):
    			result.append(matrix[j][i])
    	if len(matrix)-2*startcolumns <= 1:
    		return result
    	else:
    		for j in range(len(matrix)-startcolumns-2,startcolumns-1,-1):
    			result.append(matrix[j][i])
    	if len(matrix[0])-2*startrow-1 <= 1:
    		return result
    	else:
    		for i in range(len(matrix[0])-startrow-2,startrow,-1):
    			result.append(matrix[j][i])  	
    	return result

# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         # write code here
#         result = []
#         while(matrix):
#             result+=matrix.pop(0)
#             if not matrix or not matrix[0]:
#                 break
#             matrix = self.turn(matrix)
#         return result
#     def turn(self,matrix):
#         num_r = len(matrix)
#         num_c = len(matrix[0])
#         newmat = []
#         for i in range(num_c):
#             newmat2 = []
#             for j in range(num_r):
#                 newmat2.append(matrix[j][i])
#             newmat.append(newmat2)
#         newmat.reverse()
#         return newmat

# s = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
# s = [[1],[3],[4]]
# s = [[1,4,5]]
# s = []
s = [[1]]
t = Solution()
a = t.printMatrix(s)
print(a)
