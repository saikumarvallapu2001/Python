
price = int(input("Enter product price:"))
rating = float(input("Enter Rating for products:"))
product = input("Enter Product Name")
product_name = input("Enter Product Name")

products= list(input("Enter the list of items:"))
price_products = list(map(int, input("Enter price of product:").split()))

rate_products = list(map(float, input("Enter rating for the products:").split()))
discount = eval(input("Enter discounts on the products:"))
                
actual_price = tuple(map(int,input("Enter the actua; price after discounts:").split()))
  

all_product = print(f'product: {product_name} \n price:{price} \n Rating:')