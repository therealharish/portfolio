class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1 = {}
        dp2 = {}
        
        def f1(i, count):
            if i == n-1:
                return 0
            if (i, count) in dp1:
                return dp1[(i, count)]
            dontBuy = f1(i+1, count)
            buy = f2(i+1, count)-prices[i]
            dp1[(i, count)] = max(dontBuy, buy)
            return dp1[(i, count)]
        
        def f2(i, count):
            if i == n-1:
                return prices[n-1]
            if (i, count) in dp2:
                return dp2[i]
            dontSell = f2(i+1, count)
            sell = f1(i+1, count+1) + prices[i]
            dp2[(i, count)] = max(dontSell, sell)
            return dp2[i]
        
        return f1(0)