"""
Divide and Conquer, Sorting and Searching, and Randomized Algorithms
Programming assignment1
"""

def check_sign(x, y):
    """
    Make x and y positive
    """
    sign = 1
    if x < 0:
        x *= -1
        sign *= -1
    if y < 0:
        y *= -1
        sign *= -1
    return sign, x, y

def single_digit_multiplication(digit, number):
    """
    Compute a number and a digit
    """
    result, carry, n = 0, 0, 0
    while number > 0:
        temp = digit * (number % 10) + carry
        result += (10**n) * (temp % 10)
        carry = temp // 10
        n += 1
        number //= 10
    return result + carry * (10**n)

def grade_school(x, y):
    """
    Multiply two integers using Grade-School method
    """
    sign, x, y, = check_sign(x, y)
    result, n = 0, 0
    while x > 0:
        result += (10**n) * single_digit_multiplication(x % 10, y)
        x //= 10
        n += 1
    return sign * result

def find_n_digit(x):
    """
    Find the number of digits
    """
    n = 1
    while (x // 10) != 0:
        n += 1
        x //= 10
    return n

def karatsuba(x, y):
    """
    Multiply two integers using Karatsuba method
    """
    # remove sign
    sign, x, y, = check_sign(x, y)
    # multiply two digits
    if x < 10 and y < 10:
        return x * y
    # get the number of digits
    n = max([find_n_digit(x), find_n_digit(y)])
    # decompose x and y
    n //= 2
    a = x // (10**n)
    b = x % (10**n)
    c = y // (10**n)
    d = y % (10**n)
    # recursive calls
    first = karatsuba(a, c)
    second = karatsuba(a + b, c + d)
    third = karatsuba(b, d)
    return sign * (first * 10**(2*n) + (second - first - third) * 10**n + third)

# Test
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

assert grade_school(x, y) == x * y
assert karatsuba(x, y) == x * y
