class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        '''
        # Time complexity - O(mn)
        
        '''
        q = deque()
        GATE,WALL=0,-1
        ROWS = len(rooms)
        COLS = len(rooms[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == GATE:
                    # row, col, distance
                    q.append((row, col, 0))
        
        # BFS
        visit = set()
        while q:
            row, col, distance = q.popleft()
            direction = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in direction:
                r,c=dr+row,dc+col
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or (rooms[r][c] in [GATE,WALL]) or (r, c) in visit:
                    continue
                rooms[r][c] = min(rooms[r][c], distance + 1)
                q.append((r, c, rooms[r][c]))
                visit.add((r,c))
