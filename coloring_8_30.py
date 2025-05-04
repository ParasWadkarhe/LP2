# Function to check if it's safe to color vertex `u` with color `c`
def is_safe(graph, color, u, c):
    for v in graph[u]:
        if color[v] == c:
            return False
    return True

# Backtracking function to solve the graph coloring problem
def graph_coloring(graph, m, color, u, n):
    if u == n:
        return True
    for c in range(1, m + 1):
        if is_safe(graph, color, u, c):
            color[u] = c
            if graph_coloring(graph, m, color, u + 1, n):
                return True
            color[u] = 0  # Backtrack
    return False

# Function to solve the graph coloring problem
def solve_graph_coloring(graph, m, n):
    color = [0] * n
    if graph_coloring(graph, m, color, 0, n):
        for i in range(n):
            print(f"Vertex {i} is colored with color {color[i]}")
    else:
        print("Solution does not exist")

# ======= User Input Section =======
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of colors: "))

# Create empty adjacency list
graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))
print("Enter each edge as two space-separated vertices (e.g., 0 1):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Solve the problem
solve_graph_coloring(graph, m, n)
