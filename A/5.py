def fractional_knapsack(capacity, items):

    # Sort items by profit/weight ratio in descending order
    items.sort(key=lambda x: x["profit"] / x["weight"], reverse=True)

    total_profit = 0

    for item in items:
        if capacity <= 0:
            break

        if item["weight"] <= capacity:
            capacity -= item["weight"]
            total_profit += item["profit"]

            print("Taken full item: Profit =", item["profit"])

        else:
            fraction = capacity / item["weight"]
            profit = item["profit"] * fraction
            total_profit += profit

            print(f"Taken fraction: Profit = {profit:.2f}")
            capacity = 0

    return total_profit

# Main program
capacity = float(input("Enter knapsack capacity: "))
n = int(input("Enter number of items: "))

items = []

for i in range(n):
    print(f"\nItem {i + 1}")

    profit = float(input("Enter profit: "))
    weight = float(input("Enter weight: "))

    if profit < 0 or weight <= 0:
        print("Invalid profit or weight!")
        break

    items.append({"profit": profit, "weight": weight})

else:
    if capacity < 0:
        print("Invalid capacity!")
    else:
        result = fractional_knapsack(capacity, items)
        print(f"\nMaximum profit = {result:.2f}")