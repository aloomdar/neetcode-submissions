class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a result array
        # initialize each value in the res array to 1 so there is something to multiply
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            # res right now is technically the prefix array 
            # so I am getting the prefix array values
            res[i] = prefix
            # Multiply the prefix by the value of num at index i
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            # I am multiplying now because we have each value in the array
            # and I don't want to overwrite the values
            res[i] *= postfix
            # Multiply the postfix by the value of num at index i
            postfix *= nums[i]
        return res


        