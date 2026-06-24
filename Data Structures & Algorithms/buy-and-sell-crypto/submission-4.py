class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## TWO POINTERS | time: O(n), space: O(1)
        # if buy price > sell price, negative money, sell price = buy price
        # if buy price < sell price, compute max profit, search more optimal one
        buy, sell = 0, 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] >= prices[sell]:
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            sell += 1
        return maxProfit

        ## BRUTE FORCE | time: O(n^2), space: O(1)
        # for each buy price, find optimal sell price & store best profit 
        buy = sell = prices[0]
        maxProfit = 0
        
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                maxProfit = max(maxProfit, sell - buy)
        return maxProfit
        