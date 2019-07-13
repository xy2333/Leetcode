# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def Digalsum(x):
        	sums = 0
        	while x > 0:
        		sums += x%10
        		x = x//10
        	return sums

        def move_back(begin_row,begin_col,threshold,rows,cols):
        	if begin_col >= cols or begin_row >= rows or begin_row < 0 or begin_col < 0 or Digalsum(begin_col)+Digalsum(begin_row) > threshold or [begin_row,begin_col] in vis:
        		return 0
        	vis.append([begin_row,begin_col])
        	return 1 + move_back(begin_row+1, begin_col, threshold, rows, cols) + move_back(begin_row-1, begin_col, threshold, rows, cols) + move_back(begin_row, begin_col+1, threshold, rows, cols) + move_back(begin_row, begin_col-1, threshold, rows, cols) 

        vis = []
        return move_back(0,0, threshold, rows, cols)



t = Solution()
a = t.movingCount(5,5,5)
print(a)