a = 50
def name():
    print("from module call ")

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
def mod(x, y):
    return x % y
def floordiv(x, y):
    return x // y
def power(x, y):
    return x ** y
def sqrt(x):
    return x ** 0.5
def cube(x):
    return x ** 3
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
def lcm(x, y):
    return (x * y) // gcd(x, y)
def percentage(total, part):
    return (part / total) * 100
def average(numbers):
    return sum(numbers) / len(numbers)
def max_num(numbers):
    return max(numbers)
def min_num(numbers):
    return min(numbers)
def circle_area(radius):
    import math
    return math.pi * radius * radius
def circle_circumference(radius):
    import math
    return 2 * math.pi * radius
def rectangle_area(length, width):
    return length * width
def rectangle_perimeter(length, width):
    return 2 * (length + width)
def triangle_area(base, height):
    return 0.5 * base * height
def triangle_perimeter(a, b, c):
    return a + b + c
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def km_to_miles(km):
    return km * 0.621371
def miles_to_km(miles):
    return miles / 0.621371
def inches_to_cm(inches):
    return inches * 2.54
def cm_to_inches(cm):
    return cm / 2.54
def pounds_to_kg(pounds):
    return pounds * 0.453592
def kg_to_pounds(kg):
    return kg / 0.453592
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal
def bmi(weight, height):
    return weight / (height ** 2)
def triplet_sum(arr, target_sum):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    return True
    return False
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]
def is_palindrome(s):
    return s == s[::-1]
def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
def count_consonants(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num
def decimal_to_binary(n):
    return bin(n).replace("0b", "")
def binary_to_decimal(b):
    return int(b, 2)
def decimal_to_octal(n):
    return oct(n).replace("0o", "")
def octal_to_decimal(o):
    return int(o, 8)
def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")
def hexadecimal_to_decimal(h):
    return int(h, 16)
def day_of_week(day, month, year):
    import datetime
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = datetime.date(year, month, day).weekday()
    return days[day_index]
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6
def sum_of_cubes(n):
    return (n * (n + 1) // 2) ** 2
def harmonic_number(n):
    harmonic_sum = 0.0
    for i in range(1, n + 1):
        harmonic_sum += 1 / i
    return harmonic_sum
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
def chinese_remainder_theorem(a1, a2, m1, m2):
    M = m1 * m2
    M1 = M // m1
    M2 = M // m2
    inv1 = mod_inverse(M1, m1)
    inv2 = mod_inverse(M2, m2)
    x = (a1 * M1 * inv1 + a2 * M2 * inv2) % M
    return x
def josephus_problem(n, k):
    if n == 1:
        return 0
    else:
        return (josephus_problem(n - 1, k) + k) % n
def bell_number(n):
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    return bell[n][0]
def catalan_number(n):
    from math import comb
    return comb(2 * n, n) // (n + 1)
def derangement(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (derangement(n - 1) + derangement(n - 2))
def monty_hall_simulation(trials):
    import random
    switch_wins = 0
    stay_wins = 0
    for _ in range(trials):
        doors = [0, 0, 1]
        random.shuffle(doors)
        choice = random.randint(0, 2)
        remaining_doors = [i for i in range(3) if i != choice and doors[i] == 0]
        host_opens = random.choice(remaining_doors)
        switch_choice = [i for i in range(3) if i != choice and i != host_opens][0]
        if doors[choice] == 1:
            stay_wins += 1
        if doors[switch_choice] == 1:
            switch_wins += 1
    return switch_wins, stay_wins   
def quadratic_roots(a, b, c):
    import cmath
    d = (b ** 2) - (4 * a * c)
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    return root1, root2
def arithmetic_progression(a, d, n):
    return [a + i * d for i in range(n)]
def geometric_progression(a, r, n):
    return [a * (r ** i) for i in range(n)]

def harmonic_progression(a, d, n):
    return [1 / (a + i * d) for i in range(n)]
def lcm_multiple(numbers):
    from functools import reduce
    def lcm(x, y):
        return (x * y) // gcd(x, y)
    return reduce(lcm, numbers)
def gcd_multiple(numbers):
    from functools import reduce
    return reduce(gcd, numbers)
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
def product_of_natural_numbers(n):
    return (n * (n + 1)) // 2 ** 2
def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n
def armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
def sum_of_armstrong_numbers_in_range(start, end):
    armstrong_numbers = armstrong_numbers_in_range(start, end)
    return sum(armstrong_numbers)
def collatz_conjecture_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
def pascal_triangle_row(n):
    row = [1]
    for k in range(1, n + 1):
        row.append(row[k - 1] * (n - k + 1) // k)
    return row
def pascal_triangle_nth_row(n):
    return pascal_triangle_row(n)
def sum_of_factorials(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total
def product_of_factorials(n):
    product = 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        product *= fact
    return product
def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
def perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers
def sum_of_perfect_numbers_in_range(start, end):
    perfect_numbers = perfect_numbers_in_range(start, end)
    return sum(perfect_numbers)
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
        return fib_sequence
def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
def sum_of_fibonacci(n):
    fib_sequence = fibonacci_iterative(n)
    return sum(fib_sequence)
def product_of_fibonacci(n):
    fib_sequence = fibonacci_iterative(n)
    product = 1
    for num in fib_sequence:
        product *= num
    return product
def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def lucas_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(lucas_number(i))
    return sequence
def sum_of_lucas(n):
    lucas_seq = lucas_sequence(n)
    return sum(lucas_seq)
def product_of_lucas(n):
    lucas_seq = lucas_sequence(n)
    product = 1
    for num in lucas_seq:
        product *= num
    return product
def nth_lucas(n):
    return lucas_number(n)
def tribonacci_number(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
def tribonacci_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(tribonacci_number(i))
    return sequence
def sum_of_tribonacci(n):
    trib_seq = tribonacci_sequence(n)
    return sum(trib_seq)
def product_of_tribonacci(n):

    trib_seq = tribonacci_sequence(n)
    product = 1
    for num in trib_seq:
        product *= num
    return product
def nth_tribonacci(n):
    return tribonacci_number(n)

def square_number(n):
    return n * n
def cube_number(n):
    return n * n * n    
def is_perfect_square(n):
    root = int(n**0.5)
    return root * root == n
def is_perfect_cube(n):
    root = round(n ** (1/3))
    return root * root * root == n
def sum_of_squares_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num * num
    return total
def sum_of_cubes_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num * num * num
    return total
def multiplication_table(n, upto=10):
    table = []
    for i in range(1, upto + 1):
        table.append(f"{n} x {i} = {n * i}")
    return table
def is_even(n):
    return n % 2 == 0
def is_odd(n):
    return n % 2 != 0
def sum_of_even_numbers_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_even(num):
            total += num
    return total
def sum_of_odd_numbers_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_odd(num):
            total += num
    return total
def count_even_numbers_in_range(start, end):    
    count = 0
    for num in range(start, end + 1):
        if is_even(num):
            count += 1
    return count

def count_odd_numbers_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_odd(num):
            count += 1
    return count
def sum_of_digits_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += sum_of_digits(num)
    return total
def product_of_digits_in_range(start, end):
    product = 1
    for num in range(start, end + 1):
        n = num
        while n > 0:
            product *= n % 10
            n //= 10
    return product
def reverse_string_in_range(strings):
    reversed_strings = []
    for s in strings:
        reversed_strings.append(reverse_string(s))
    return reversed_strings
def count_vowels_in_range(strings):
    total_count = 0
    for s in strings:
        total_count += count_vowels(s)
    return total_count
def count_consonants_in_range(strings):
    total_count = 0
    for s in strings:
        total_count += count_consonants(s)
    return total_count
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
