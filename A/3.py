def insertion_sort(products):
    comparisons = 0

    for i in range(1, len(products)):
        key = products[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if products[j]["Price"] > key["Price"]:
                products[j + 1] = products[j]
                j -= 1
            else:
                break

        products[j + 1] = key

    return products, comparisons


# Product details
products = [
    {"ProductID": "P101", "Name": "Mouse", "Price": 2500},
    {"ProductID": "P102", "Name": "Laptop", "Price": 50000},
    {"ProductID": "P103", "Name": "Headphones", "Price": 4500},
    {"ProductID": "P104", "Name": "Keyboard", "Price": 1500},
    {"ProductID": "P105", "Name": "Laptop Stand", "Price": 2500}
]

# Sort products by price
sorted_products, comparisons = insertion_sort(products.copy())

# Display sorted products
print("Products sorted by price:")
for product in sorted_products:
    print(
        product["ProductID"],
        product["Name"],
        "₹" + str(product["Price"])
    )

print("\nTotal Comparisons:", comparisons)