product1 = input("Enter  product name: ")
price1 = int(input("Enter first product price: "))
rating1 = float(input("Enter first product rating: "))
discount1 = input("Enter first product discount (e.g., 10%): ")
actual_price1 = int(input("Enter first product actual price after discount: "))

product2 = input("Enter second product name: ")
price2 = int(input("Enter second product price: "))
rating2 = float(input("Enter second product rating: "))
discount2 = input("Enter second product discount (e.g., 15%): ")
actual_price2 = int(input("Enter second product actual price after discount: "))

# Storing details in a dictionary
products = {
    product1: {"Price": price1, "Rating": rating1, "Discount": discount1, "Actual Price": actual_price1},
    product2: {"Price": price2, "Rating": rating2, "Discount": discount2, "Actual Price": actual_price2}
}
products = eval(input())
print(product1, price1, rating1, discount1,actual_price1,sep='\n', end='\n Details are displayed for product 1 \n')

print(product2, price2, rating2, discount2, actual_price2, sep='\n')
 
