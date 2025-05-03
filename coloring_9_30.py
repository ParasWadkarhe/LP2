# Function to check if it's safe to color vertex `u` with color `c`
def is_safe(graph, color, u, c):
    for v in graph[u]:
        if color[v] == c:
            return False
    return True

# Backtracking function to solve the graph coloring problem
def graph_coloring(graph, m, color, u, n):
    # If all vertices are assigned a color then return True
    if u == n:
        return True

    # Try different colors for vertex `u`
    for c in range(1, m+1):
        if is_safe(graph, color, u, c):
            color[u] = c  # Assign color `c` to vertex `u`
            if graph_coloring(graph, m, color, u+1, n):
                return True
            color[u] = 0  # Backtrack

    return False

# Function to solve the graph coloring problem
def solve_graph_coloring(graph, m, n):
    color = [0] * n  # Color assignment for each vertex
    if graph_coloring(graph, m, color, 0, n):
        for i in range(n):
            print(f"Vertex {i} is colored with color {color[i]}")
    else:
        print("Solution does not exist")

# Example graph (adjacency list)
graph = [
    [1, 3],    # Vertex 0
    [0, 2, 4], # Vertex 1
    [1],       # Vertex 2
    [0, 4],    # Vertex 3
    [1, 3]     # Vertex 4
]

# Number of vertices
n = len(graph)
# Maximum number of colors
m = 3

# Solve the graph coloring problem
solve_graph_coloring(graph, m, n)
