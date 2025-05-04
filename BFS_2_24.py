from collections import deque

# Create graph from user input
graph = {}
n = int(input("Enter number of vertices: "))

print("Enter vertex names:")
vertices = [input(f"Vertex {i+1}: ") for i in range(n)]

for vertex in vertices:
    graph[vertex] = []

e = int(input("Enter number of edges: "))
print("Enter edges (undirected) in the format: vertex1 vertex2")
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

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

# Start BFS from user input
start_node = input("Enter starting node for BFS: ")
visited.add(start_node)
queue = deque([start_node])

print("Breadth First Search traversal:")
bfs_recursive(queue)


# Enter number of vertices: 6
# Vertex 1: A
# Vertex 2: B
# Vertex 3: C
# Vertex 4: D
# Vertex 5: E
# Vertex 6: F
# Enter number of edges: 6
# A B
# A C
# B D
# B E
# C F
# E F
# Enter starting node for BFS: A
