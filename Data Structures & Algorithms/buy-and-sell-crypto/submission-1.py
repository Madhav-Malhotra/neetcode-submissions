class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Validation
        if len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_prof = 0

        for i in range(1, len(prices)):
            curr = prices[i]
            prof = curr - min_price
            if prof > max_prof: 
                max_prof = prof

            if curr < min_price: 
                min_price = curr
        
        return max_prof

