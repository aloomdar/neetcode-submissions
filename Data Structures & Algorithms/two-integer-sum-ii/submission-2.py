class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create 2 pointers at start/l and end/r
        l, r = 0, len(numbers) - 1
        
        # make sure that left doesnt pass right
        while l < r:
            # store the current sum in a variable
            cursum = numbers[r] + numbers[l]

            # check if the current sum is greater or less than the target
            # if the current sum is greater, we decrement r
            # if current sum is less than the target, we increment r
            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                # we add 1 because we want the 1 indexed position
                # if it is 0 indexed, we dont add anything
                return [l + 1, r + 1]
        
        return []
