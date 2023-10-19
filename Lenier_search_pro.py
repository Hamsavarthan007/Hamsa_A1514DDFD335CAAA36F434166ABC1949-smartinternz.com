def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Sample list of products
products = ["apple", "banana", "orange", "apple", "grape", "apple"]

# Get user input for the target product
target = input("Enter the product you want to search for: ")

# Call the linear_search_product function
result = linear_search_product(products, target)

# Display the result
if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")
