
# Quick Sort and Merge Sort using Divide and Conquer

# Quick Sort
def quick_sort(arr, count):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    right = []

    for x in arr:
        if x == pivot:
            continue

        count[0] += 1

        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left, count) + [pivot] + quick_sort(right, count)


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


# Main program
n = int(input("Enter number of elements: "))

if n < 0:
    print("Count cannot be negative.")

else:
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    print("Original array:", arr)

    print("1. Quick Sort")
    print("2. Merge Sort")

    choice = int(input("Enter choice: "))

    count = [0]

    if choice == 1:
        result = quick_sort(arr.copy(), count)

    elif choice == 2:
        result = merge_sort(arr.copy(), count)

    else:
        print("Invalid choice.")
        result = None

    if result is not None:
        print("Sorted array:", result)
        print("Total comparisons:", count[0])
