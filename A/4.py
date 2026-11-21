def find_min_max(arr, low, high):

    # Single element
    if low == high:
        return arr[low], arr[low], 0

    # Two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high], 1
        else:
            return arr[high], arr[low], 1

    # Divide the array
    mid = (low + high) // 2

    left_min, left_max, left_steps = find_min_max(arr, low, mid)
    right_min, right_max, right_steps = find_min_max(arr, mid + 1, high)

    # Combine the results
    mn = min(left_min, right_min)
    mx = max(left_max, right_max)

    steps = left_steps + right_steps + 2

    print(f"Combine: min({left_min}, {right_min})={mn}, "
          f"max({left_max}, {right_max})={mx}")

    return mn, mx, steps


# Main program
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Error: Array must not be empty.")

else:
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter number {i + 1}: ")))

    mn, mx, steps = find_min_max(arr, 0, n - 1)

    print("\n---- RESULTS ----")
    print("Array:", arr)
    print("Size:", n)
    print("Minimum Element:", mn)
    print("Maximum Element:", mx)
    print("Total Comparisons:", steps)
    print("Time Complexity: O(n)")