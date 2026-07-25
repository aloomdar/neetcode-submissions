class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set for the nums because sets have O(1)/instant lookup time
        numset = set(nums)
        longest = 0

        for num in numset:
            # check if the num is the start of the sequence
            # if num is start of the sequence, length is 1
            if num - 1 not in numset:
                length = 1
                # create a while loop and keep adding length to num
                # to check if the next consecutive number is in the set
                while num + length in numset:
                    length += 1
                # if the next consecutive value is not in the set then get the max
                # value. Length might be longer than longest once we find a new
                # sequence
                longest = max(length, longest)
        return longest

            