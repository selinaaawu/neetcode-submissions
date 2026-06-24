class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        ## BRUTE FORCE
        # for each buy price, find optimal sell price
        # store best profit 
        buy = sell = prices[0]
        maxProfit = 0
        
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                maxProfit = max(maxProfit, sell - buy)
        return maxProfit

        