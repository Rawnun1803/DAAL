def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    return True


def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n

    mst = []
    cost = 0

    # Sort edges by weight
    edges.sort()

    print("\nSorted edges:", edges)

    for w, u, v in edges:
        print(f"\nChecking edge ({u}-{v}), weight {w}")

        if union(parent, rank, u, v):
            mst.append((u, v, w))
            cost += w

            print("Accepted")
            print("MST so far:", mst, "| Cost:", cost)
        else:
            print("Rejected: forms a cycle")

        if len(mst) == n - 1:
            break

    if len(mst) != n - 1:
        print("\nWarning: Graph is disconnected!")

    return mst, cost


# Main program
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))

edges = []

print("Enter each edge: u v weight")

for i in range(m):
    u, v, w = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((w, u, v))

mst, cost = kruskal(n, edges)

print("\n--- Minimum Spanning Tree ---")

for u, v, w in mst:
    print(f"Edge ({u} - {v}) with weight {w}")

print("Total Minimum Cost:", cost)