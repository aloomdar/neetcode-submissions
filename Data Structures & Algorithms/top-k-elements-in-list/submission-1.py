class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a count map to keep track of the number of times a number shows up
        count = {}
        # I create a frequency list where the index is the number of occurences and we add 1 because the list is 0 indexed 
        # so it would be 1 less if I didnt add 1
        freq = [[] for i in range(len(nums) + 1)]

        # populate the count map with the number as the key and the number of occurences as the value
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        # n is number and c is count
        # for every number and count, I want to append the count as the key and the number as the value
        # I do this because I want to iterate throught the list at the end in descending order until the res is the same length
        # as k
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        # im going to iterate throught freq in descending order, which is what the -1 is
        # len(freq) - 1 is the last index and we go until we get 0
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
