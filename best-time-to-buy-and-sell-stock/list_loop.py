class Solution:
    def maxProfit(self, prices):
        profit=0
        minimum=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<=minimum:
                minimum=prices[i]
            elif prices[i]>minimum:
                a=prices[i]-minimum
                if a>profit:
                    profit=a
        return profit
s1=Solution()
print(s1.maxProfit([7,1,5,3,6,4]))