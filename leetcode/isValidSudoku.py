class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		row = [{} for i in range(9)]
		col = [{} for i in range(9)]
		box = [{} for i in range(9)]
		for i in range(9):
			for j in range(9):
				if board[i][j] == '.':
					pass
				elif board[i][j] not in row[i]:
					row[i][board[i][j]] = 0
				else:
					return False
				if board[i][j] == '.':
					pass
				elif board[i][j] not in col[j]:
					col[j][board[i][j]] = 0
				else:
					return False
				if board[i][j] == '.':
					pass
				elif board[i][j] not in box[(i//3)*3+j//3]:
					box[(i//3)*3+j//3][board[i][j]] = 0
				else:
					return False
		return True


        
        

        
        

s = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]


t = Solution()
res = t.isValidSudoku(s)
print(res)


