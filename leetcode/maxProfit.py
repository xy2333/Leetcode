class Solution:
	def maxProfit(self, prices):
		if len(prices) <= 1:
			return 0
		maxprofit = 0
		minrise = prices[0]
		for i in range(1,len(prices)):
			if prices[i] < minrise:
				minrise = prices[i]
			else:
				maxprofit = max(maxprofit,prices[i]-minrise)
		return maxprofit