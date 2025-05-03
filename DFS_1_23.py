# Create the graph using adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Keep track of visited nodes
visited = set()

# Recursive DFS function
def dfs(vertex):
    if vertex not in visited:
        print(vertex, end=' ')  # Visit the node
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(neighbor)

# Call DFS starting from a node
print("Depth First Search traversal:")
dfs('A')
