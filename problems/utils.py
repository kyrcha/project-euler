import math  

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def is_palindrome(string):
    isit = True
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            isit = False
    return isit

def is_n_pandigital(n):
    as_string = str(n)
    length = len(as_string)
    for i in range(1, length + 1):
        as_string = as_string.replace(str(i), '', 1)
    if len(as_string) > 0:
        return False
    else:
        return True

def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

def tobinary(n):
    binary = bin(n)
    return binary[2:len(binary)]

def return_divisors(n):
    divisors = []
    i = 1
    while i <= math.sqrt(n): 
        if n % i == 0: 
            if n / i == i: 
                divisors.append(i)
            else: 
                divisors.append(i)
                divisors.append(int(n/i))
        i = i + 1
    return divisors

def return_proper_divisors(n):
    temp = return_divisors(n)
    return [i for i in temp if i != n]

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def is_abundant(n):
    sum_proper_divs = sum_list(return_proper_divisors(n))
    if sum_proper_divs > n:
        return True
    else:
        return False
