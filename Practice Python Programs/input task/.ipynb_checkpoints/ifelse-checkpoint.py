products = []  # List to store added products
cart = []  # List to store cart items
users = {}  # Dictionary to store user details dynamically

# Admin or User login
user_id = input("Enter ID: ")
password = input("Enter Password: ")

if user_id == "admin" and password == "admin123":
    print("Welcome, Admin!")
    print("Add products to the store")
    
    for i in range(5):  # Admin can add up to 5 products
        product = input(f"Enter product {i+1} name (or type 'done' to stop): ")
        if product.lower() == 'done':
            break
        products.append(product)
    
    print("Products added successfully!")
    print("Available Products:", products)

elif user_id != "admin":
    if user_id not in users:
        print("Welcome, New User!")
        username = input("Enter your name: ")
        email = input("Enter your email: ")
        users[user_id] = {'name': username, 'email': email}
    
    print(f"Hello {users[user_id]['name']}, browse and add products to your cart.")
    
    if not products:
        print("No products available. Please wait for the admin to add products.")
    else:
        for product in products:
            choice = input(f"Do you want to add '{product}' to your cart? (yes/skip): ")
            if choice.lower() == "yes":
                cart.append(product)
        
        if cart:
            print("Your Cart:", cart)
        else:
            print("Your cart is empty.")

else:
    print("Invalid credentials! Please try again.")
