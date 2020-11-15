class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1: return 0
        res = 0
        
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
                
        return res