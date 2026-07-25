class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize the left and right pointers to the first and second day (0 and 1)
        l, r = 0, 1
        maxp = 0

        # while the right pointer is less than the length of prices, we check if the price
        # of the left pointer is less than the right pointer
        # if left is less than right, we set the max profit to the max of the current max profit
        # and the price difference of the right minus left
        # if right is less than left, we set left to the new minimum 
        # we keep incrementing right to reach the end of the list to continue the loop
        while r < len(prices):
            if prices[l] < prices[r]:
                maxp = max(maxp, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return maxp