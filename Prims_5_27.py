import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost
        print(f"Add edge with cost {cost} to node {u}")
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (weight, v))

    print("Total cost of MST:", total_cost)

# --- User Input Section ---
graph = {}
n = int(input("Enter number of nodes: "))

print("Enter node names:")
nodes = [input(f"Node {i+1}: ") for i in range(n)]

for node in nodes:
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter edges in format: from to weight")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))  # since it's an undirected graph

start_node = input("Enter the starting node: ")
prim_mst(graph, start_node)


# Enter number of nodes: 4
# Node 1: A
# Node 2: B
# Node 3: C
# Node 4: D
# Enter number of edges: 5
# Enter edges in format: from to weight
# A B 2
# A C 3
# B C 1
# B D 1
# C D 4
# Enter the starting node: A
