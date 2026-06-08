class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price of NeetCoin on ith day
        # choose one day to buy one day to sell
        # return max profit, can be 0

        ## TWO POINTER SLIDING WINDOW | O(N)
        maxProfit = 0

        buy, sell = 0, 1
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            sell += 1
        return maxProfit

        ## IDK
        maxProfit = 0
        buy = prices[0]
        sell = prices[1]
        for i in range(len(prices) - 1 ):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i + 1]
            elif prices[i] > sell:
                sell = prices[i]
            maxProfit = max(maxProfit, sell - buy)
        return maxProfit
        