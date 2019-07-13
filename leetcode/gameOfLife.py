class Solution(object):
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""
		temp = [[0]*len(board[0]) for i in range(len(board))]
		for i in range(len(board)):
			for j in range(len(board[0])):
				num = 0
				if i-1 >= 0:
					if board[i-1][j] == 1:
						num += 1
					if j-1 >= 0:
						if board[i-1][j-1] == 1:
							num += 1
					if j+1 < len(board[0]):
						if board[i-1][j+1] == 1:
							num += 1
				if j-1 >= 0 and board[i][j-1] == 1:
					num += 1
				if j+1 < len(board[0]) and board[i][j+1] == 1:
					num += 1
				if i+1 < len(board):
					if board[i+1][j] == 1:
						num += 1
					if j-1 >= 0:
						if board[i+1][j-1] == 1:
							num += 1
					if j+1 < len(board[0]):
						if board[i+1][j+1] == 1:
							num += 1		
				if board[i][j] == 1:
					if num < 2:
						temp[i][j] = 0
					elif num == 2 or num == 3:
						temp[i][j] = 1
					else:
						temp[i][j] = 0
				else:
					if num == 3:
						temp[i][j] = 1
					else:
						temp[i][j] = 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				board[i][j] = temp[i][j]

		return board





t = Solution()
s = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

res = t.gameOfLife(s)
print(res)
