from collections import deque

# Undirected graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Set to keep track of visited nodes
visited = set()

# Recursive BFS function
def bfs_recursive(queue):
    if not queue:
        return
    
    vertex = queue.popleft()
    print(vertex, end=' ')
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    bfs_recursive(queue)

# Start BFS from a given node
start_node = 'A'
visited.add(start_node)
queue = deque([start_node])

print("Breadth First Search traversal:")
bfs_recursive(queue)
