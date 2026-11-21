import heapq

def prim(graph, start):
    visited = set()
    mst = []
    cost = 0

    heap = [(0, start, None)]
    step = 1

    print("\n--- Intermediate Steps ---")

    while heap:
        print(f"\nStep {step}: Heap = {heap}")

        w, u, parent = heapq.heappop(heap)

        if u in visited:
            print(f"Skip {u}: already visited")
            step += 1
            continue

        visited.add(u)
        cost += w

        if parent is not None:
            mst.append((parent, u, w))
            print(f"Selected edge: {parent}-{u}, weight={w}")
        else:
            print(f"Starting node: {u}")

        print("Visited:", visited)
        print("MST so far:", mst)
        print("Total cost:", cost)

        for v, weight in graph.get(u, []):
            if v not in visited:
                heapq.heappush(heap, (weight, v, u))

        print("Heap after adding neighbors:", heap)
        step += 1

    if len(visited) != len(graph):
        print("\nWarning: Graph is disconnected!")

    return mst, cost


# Main program
graph = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u, v, w = input("Enter edge (A B 4): ").split()
    w = int(w)

    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))

start = input("Enter starting node: ").strip()

if start not in graph:
    print("Invalid starting node!")
else:
    mst, cost = prim(graph, start)

    print("\n--- Minimum Spanning Tree ---")
    print("MST Edges:", mst)
    print("Total Minimum Cost:", cost)