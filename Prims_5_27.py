import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (cost, node)
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

# Example graph as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

prim_mst(graph, 'A')
