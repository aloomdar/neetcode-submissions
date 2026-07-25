class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = abs(r-l) * min(heights[l], heights[r])

        while l < r:
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1 
            
            if maxArea < abs(r-l)*min(heights[l], heights[r]):
                maxArea = abs(r-l)*min(heights[l], heights[r])
        return maxArea