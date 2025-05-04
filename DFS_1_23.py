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
    graph[v].append(u)  # because the graph is undirected

# DFS implementation
visited = set()

def dfs(vertex):
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(neighbor)

# Start DFS from user-defined node
start = input("Enter starting node for DFS: ")
print("Depth First Search traversal:")
dfs(start)



# Enter number of vertices: 6
# Vertex 1: A
# Vertex 2: B
# Vertex 3: C
# Vertex 4: D
# Vertex 5: E
# Vertex 6: F
# Enter number of edges: 6
# Enter edges (undirected) in the format: vertex1 vertex2
# A B
# A C
# B D
# B E
# C F
# E F
# Enter starting node for DFS: A
