# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self,matrix,rows,cols,path):
        def path_back(lmatrix,rows,cols,path,i,j,temp):
            # 此处注意全局变量和局部变量的差别，经过x = list(temp)的一波操作，x变为局部变量，函数内的x值变化不会引起函数外x值的变化；如果一直使用temp的话，会默认temp为全局变量，无法回溯
            x = list(temp)
            if not path:
                return True
            if i >= rows or j >= cols or i < 0 or j < 0 or x[i*cols+j] == 1 or lmatrix[i*cols+j] != path[0]:
                return False
            x[i*cols+j] = 1
            return path_back(lmatrix,rows,cols,path[1:],i+1,j,x) or path_back(lmatrix,rows,cols,path[1:],i-1,j,x) or path_back(lmatrix,rows,cols,path[1:],i,j-1,x) or path_back(lmatrix,rows,cols,path[1:],i,j+1,x)

        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    temp = [0]*len(matrix)
                    if path_back(list(matrix),rows,cols,path,i,j,temp):
                        return True
        return False





t = Solution()
s = 'abcebfcsadee'
a = t.hasPath(s,3,4,'abccfb')
print(a)