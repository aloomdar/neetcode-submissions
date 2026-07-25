class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a res list and sort the numbers
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # i am checking if we are not at the first index and if the value a is the same as the previous number
            # if a is the same value as the previous number, we continue to the next interation of the loop
            if i > 0 and a == nums[i - 1]:
                continue

            # create a left and right pointer, left is going to be the next number after "a"
            # right is the last number in the list
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                # I reach this else block when threeSum is 0 so i append it to res
                else:
                    res.append([a, nums[l], nums[r]])
                    """
                    I increment left by 1 and create a while loop that keeps increasing 
                    the left pointer by 1 as long as it is the same as the previous value and while
                    left is less than right
                    """
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+= 1
        
        return res
        