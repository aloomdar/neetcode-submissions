class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for i, n in enumerate(nums):
            idxs[n] = i
        for i, n in enumerate(nums):
            complement = target - n
            if complement in idxs and idxs[complement] != i:
                return [i, idxs[complement]]
        return []
        