class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols =  len(grid), len(grid[0])
        islands = 0

        moves = [(0,1), (0, -1), (1,0), (-1,0)]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for x, y in moves:
                dfs(row + x, col + y)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands


        