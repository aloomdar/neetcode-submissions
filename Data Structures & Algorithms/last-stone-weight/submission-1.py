class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # I want to create a max heap so I get the negative values because when I heapify the list, 
        # it will sort the heap into ascending order
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # I keep doing this until the length of the stones list is one because there should be 1 stone left
        while len(stones) > 1:
            # I do -heapq because I made the original values negative in order to create a max heap since 
            # heapify creates a min heap by default. I'm just restoring the weights back to their original wieight
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, y - x)
        # I append 0 in case no stones remain 
        stones.append(0)
        return abs(stones[0])
        

        