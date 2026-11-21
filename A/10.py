import heapq

def calculate_bound(path, cost, adj, n):
    unvisited = [i for i in range(n) if i not in path]

    bound = cost
    current = path[-1]

    if unvisited:
        bound += min(adj[current][v] for v in unvisited)

        for v in unvisited:
            bound += min(adj[v][j] for j in range(n) if j != v)

    return bound


def tsp_branch_bound(adj):
    n = len(adj)
    best_cost = float('inf')
    best_path = []
    steps = 0

    pq = [(calculate_bound([0], 0, adj, n), 0, [0])]

    while pq:
        bound, cost, path = heapq.heappop(pq)
        steps += 1

        print(f"\nStep {steps}: Path={path}, Cost={cost}, Bound={bound}")

        if bound >= best_cost:
            print("Pruned")
            continue

        if len(path) == n:
            total = cost + adj[path[-1]][0]

            if total < best_cost:
                best_cost = total
                best_path = path + [0]

            continue

        for v in range(n):
            if v not in path:
                new_path = path + [v]
                new_cost = cost + adj[path[-1]][v]

                new_bound = calculate_bound(new_path, new_cost, adj, n)

                if new_bound < best_cost:
                    heapq.heappush(pq, (new_bound, new_cost, new_path))
                    print("Added:", new_path)
                else:
                    print("Pruned:", new_path)

    return best_path, best_cost, steps


# Main program
n = int(input("Enter number of cities: "))

if n < 2:
    print("Enter at least 2 cities.")

else:
    adj = []

    print("Enter cost matrix row by row:")

    for i in range(n):
        row = list(map(int, input().split()))

        if len(row) != n:
            print("Invalid row length!")
            break

        adj.append(row)

    else:
        path, cost, steps = tsp_branch_bound(adj)

        print("\n--- Results ---")

        if path:
            print("Optimal Path:", " -> ".join(map(str, path)))
            print("Minimum Cost:", cost)
        else:
            print("No valid tour found.")

        print("Total Steps:", steps)