from problem import *


print("Welcome to Smart Math Validator!")
    
while True:
    print("\nChoose an option:")
    print("1. Check Prime Number")
    print("2. Calculate Factorial")
    print("3. Generate Fibonacci Sequence")
    print("4. Find GCD (Greatest Common Divisor)")
    print("5. Find LCM (Least Common Multiple)")
    print("6. Sum of Digits")
    print("7. Reverse a Number")
    print("8. Check Palindrome Number")
    print("9. Check Armstrong Number")
    print("10. Check Perfect Number")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("Enter a number: "))
        print(f"{num} is Prime: {prime(num)}")
    elif choice == "2":
        num = int(input("Enter a number: "))
        print(f"Factorial of {num}: {factorial(num)}")

    elif choice == "3":
        num = int(input("Enter the number of Fibonacci terms: "))
        print(f"Fibonacci sequence: {fibonacci(num)}")

    elif choice == "4":
        a, b = map(int, input("Enter two numbers (space-separated): ").split())
        print(f"GCD of {a} and {b}: {gcd(a, b)}")

    elif choice == "5":
        a, b = map(int, input("Enter two numbers (space-separated): ").split())
        print(f"LCM of {a} and {b}: {lcm(a, b)}")

    elif choice == "6":
        num = int(input("Enter a number: "))
        print(f"Sum of digits: {sum_of_digits(num)}")

    elif choice == "7":
        num = int(input("Enter a number: "))
        print(f"Reversed number: {reverse_number(num)}")

    elif choice == "8":
        num = int(input("Enter a number: "))
        print(f"{num} is Palindrome: {is_palindrome(num)}")

    elif choice == "9":
        num = int(input("Enter a number: "))
        print(f"{num} is Armstrong: {is_armstrong(num)}")

    elif choice == "10":
        num = int(input("Enter a number: "))
        print(f"{num} is Perfect: {is_perfect(num)}")

    elif choice == "0":
        print("Exiting... Thank you for using Smart Math Validator!")
        break
        
    else:
        print("Invalid choice! Please try again.")

1