class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Constraints:
        #1 <= prices.length <= 100
        #0 <= prices[i] <= 100
        max_profit = 0
        least = prices[0]
        for leftwin in range(len(prices)):
            if least < prices[leftwin]:
                continue
            elif prices[leftwin] < least:
                least = prices[leftwin]
            rightwin = leftwin+1
            while rightwin < len(prices):
                if (prices[rightwin] - prices[leftwin]) < 0:
                    break
                if (prices[rightwin] - prices[leftwin]) > max_profit:
                    max_profit = prices[rightwin] - prices[leftwin]
                rightwin+=1
        return max_profit