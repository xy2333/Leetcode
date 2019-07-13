class Solution:
    # @param n, an integer
    # @return an integer
	def reverseBits(self, n):
		return int('0b'+bin(n)[2:].zfill(32)[::-1],base = 2)