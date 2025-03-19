def prime(n):
    if n <= 1:
        return f"{n} is not a prime number"
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number"
    
    return f"{n} is a prime number"

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Extract the last digit and add to total
        n //= 10         # Remove the last digit
    return total

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)  # Extract last digit and add to new number
        n //= 10  # Remove last digit
    return reversed_num

def is_palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)  # Extract last digit and build reversed number
        n //= 10  # Remove last digit
    return original == reversed_num



def is_armstrong(n):
    num_digits = len(str(n))  # Count the number of digits
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10  # Extract last digit
        total += digit ** num_digits  # Add digit^num_digits to total
        temp //= 10  # Remove last digit

    return total == n

def is_perfect(n):
    if n <= 1:
        return False
    
    sum_divisors = 1  # 1 is always a divisor
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to sqrt(n)
        if n % i == 0:
            sum_divisors += i
            if i != n // i:  # Add the corresponding divisor
                sum_divisors += n // i

    return sum_divisors == n

