
# Binary Search using Divide and Conquer

def binary_search(arr, low, high, key, step=1):

    if low > high:
        print("Element not found.")
        return -1

    mid = (low + high) // 2

    print(f"Step {step}: low={low}, high={high}, mid={mid}, value={arr[mid]}")

    if arr[mid] == key:
        print("Element found at index:", mid)
        return mid

    elif key < arr[mid]:
        print("Searching left half")
        return binary_search(arr, low, mid - 1, key, step + 1)

    else:
        print("Searching right half")
        return binary_search(arr, mid + 1, high, key, step + 1)


# Main program
n = int(input("Enter number of elements: "))

if n < 0:
    print("Invalid number of elements.")

else:
    arr = []

    for i in range(n):
        num = int(input("Enter element: "))
        arr.append(num)

    print("Original array:", arr)

    arr.sort()
    print("Sorted array:", arr)

    key = int(input("Enter element to search: "))

    result = binary_search(arr, 0, n - 1, key)

    if result != -1:
        print("Search successful!")
    else:
        print("Search unsuccessful!")
