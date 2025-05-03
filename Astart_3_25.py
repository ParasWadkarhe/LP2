import heapq

grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

start, goal = (0, 0), (2, 3)

def h(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal):
    heap = [(0, start, [])]
    seen = set()
    while heap:
        _, curr, path = heapq.heappop(heap)
        if curr in seen: continue
        seen.add(curr)
        path = path + [curr]
        if curr == goal: return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = curr[0]+dx, curr[1]+dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                heapq.heappush(heap, (len(path) + h((x, y), goal), (x, y), path))
    return []

print("Path:", astar(start, goal))
if not astar(start,goal):
    print('No path Found')
