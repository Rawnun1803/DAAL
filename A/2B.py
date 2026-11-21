
# Quick Sort and Merge Sort using Divide and Conquer

# Quick Sort
def quick_sort(arr, count, choice):

    if len(arr) <= 1:
        return arr

    # Select pivot
    if choice == 1:
        p = 0
    elif choice == 2:
        p = len(arr) // 2
    else:
        p = len(arr) - 1

    pivot = arr[p]

    left = []
    right = []

    for i, x in enumerate(arr):

        if i == p:
            continue

        count[0] += 1

        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return (quick_sort(left, count, choice)
            + [pivot]
            + quick_sort(right, count, choice))


# Merge Sort
def merge_sort(arr, count):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], count)
    right = merge_sort(arr[mid:], count)

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        count[0] += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


# Main Program
n = int(input("Enter number of elements: "))

if n < 0:
    print("Count cannot be negative.")

else:
    arr = []

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        arr.append(num)

    print("Original array:", arr)

    print("\n1. Quick Sort")
    print("2. Merge Sort")

    choice = int(input("Enter choice: "))

    count = [0]
    result = None

    if choice == 1:

        print("\nChoose Pivot:")
        print("1. Beginning")
        print("2. Middle")
        print("3. End")

        p = int(input("Enter pivot choice: "))

        if p in (1, 2, 3):
            result = quick_sort(arr.copy(), count, p)
        else:
            print("Invalid pivot choice.")

    elif choice == 2:
        result = merge_sort(arr.copy(), count)

    else:
        print("Invalid choice.")

    if result is not None:
        print("\nSorted array:", result)
        print("Total comparisons:", count[0])
