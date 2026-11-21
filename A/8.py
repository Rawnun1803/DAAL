def tsp(mask, pos):
    global steps

    # All cities visited
    if mask == (1 << n) - 1:
        return dist[pos][0]

    # Check memoization table
    if (mask, pos) in memo:
        return memo[(mask, pos)]

    best = float("inf")

    for nxt in range(n):
        if not (mask & (1 << nxt)):
            cost = dist[pos][nxt] + tsp(mask | (1 << nxt), nxt)

            if cost < best:
                best = cost
                parent[(mask, pos)] = nxt

    memo[(mask, pos)] = best
    steps += 1

    visited = [cities[i] for i in range(n) if mask & (1 << i)]

    print(f"Step {steps}: Visited={visited}, "
          f"Current={cities[pos]}, Cost={best}")

    return best


# Main program
n = int(input("Enter number of cities: "))

if n < 2:
    print("Enter at least 2 cities.")

else:
    cities = []

    for i in range(n):
        name = input(f"City {i + 1} name: ").strip()
        cities.append(name if name else f"City {i + 1}")

    print("Enter distance matrix row by row:")

    dist = []
    valid = True

    for i in range(n):
        row = list(map(float, input().split()))

        if len(row) != n or any(x < 0 for x in row):
            print("Enter exactly", n, "non-negative distances per row.")
            valid = False
            break

        dist.append(row)

    if valid:
        memo = {}
        parent = {}
        steps = 0

        full = (1 << n) - 1

        cost = tsp(1, 0)

        # Reconstruct shortest path
        route = [0]
        mask = 1
        pos = 0

        while mask != full:
            nxt = parent[(mask, pos)]
            route.append(nxt)
            mask = mask | (1 << nxt)
            pos = nxt

        route.append(0)

        print("\n--- FINAL RESULTS ---")
        print("Total unique subproblems:", steps)
        print("Shortest route:", " -> ".join(cities[i] for i in route))
        print("Minimum cost:", cost)