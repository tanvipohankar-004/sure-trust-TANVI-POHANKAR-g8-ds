# Scientific Calculator - Without using math library

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b):
    result = 0
    for _ in range(abs(int(b))): result += a
    if b < 0: result = -result
    return result

def divide(a, b): return "Error" if b == 0 else a / b

def modulus(a, b): return "Error" if b == 0 else a % b

def power(base, exponent):
    result = 1
    is_negative = False
    if exponent < 0:
        is_negative = True
        exponent = -exponent
    for _ in range(int(exponent)): result *= base
    return 1 / result if is_negative else result

def square_root(n, precision=0.0001):
    if n < 0: return "Error! Negative number."
    guess = n / 2
    while True:
        better = (guess + n / guess) / 2
        if abs(guess - better) < precision:
            return round(better, 5)
        guess = better

def factorial(n):
    if n < 0: return "Error!"
    result = 1
    for i in range(2, int(n)+1):
        result *= i
    return result

def exponential(x, terms=20):
    result = 1
    numerator = 1
    denominator = 1
    for i in range(1, terms):
        numerator *= x
        denominator *= i
        result += numerator / denominator
    return round(result, 5)

def natural_log(x, terms=100):
    if x <= 0: return "Error!"
    n = (x - 1) / (x + 1)
    result = 0
    for i in range(1, terms*2, 2):
        result += (1 / i) * power(n, i)
    return round(2 * result, 5)

def log_base_10(x):
    return round(natural_log(x) / natural_log(10), 5)

def deg_to_rad(deg):
    return deg * (3.14159 / 180)

def rad_to_deg(rad):
    return rad * (180 / 3.14159)

def sin(x):
    x = deg_to_rad(x)
    result = 0
    for i in range(10):
        sign = (-1) ** i
        result += sign * power(x, 2*i + 1) / factorial(2*i + 1)
    return round(result, 5)

def cos(x):
    x = deg_to_rad(x)
    result = 0
    for i in range(10):
        sign = (-1) ** i
        result += sign * power(x, 2*i) / factorial(2*i)
    return round(result, 5)

def tan(x):
    sin_val = sin(x)
    cos_val = cos(x)
    return "Undefined" if cos_val == 0 else round(sin_val / cos_val, 5)

def dec_to_other(num):
    num = int(num)
    return bin(num), oct(num), hex(num)

def other_to_dec(val, base):
    try:
        return int(val, base)
    except:
        return "Invalid value."

def show_main_menu():
    print("\n--- SCIENTIFIC CALCULATOR ---")
    print("1. Arithmetic Operations")
    print("2. Power & Roots")
    print("3. Factorial & Exponential")
    print("4. Logarithmic Functions")
    print("5. Trigonometric Functions")
    print("6. Angle Conversion")
    print("7. Number System Conversions")
    print("0. Exit")

def show_submenu(choice):
    if choice == 1:
        print("\n-- Arithmetic Operations --")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
    elif choice == 2:
        print("\n-- Power & Roots --")
        print("1. Power\n2. Square Root")
    elif choice == 3:
        print("\n-- Factorial & Exponential --")
        print("1. Factorial\n2. Exponential")
    elif choice == 4:
        print("\n-- Logarithmic Functions --")
        print("1. Natural Log\n2. Log Base 10")
    elif choice == 5:
        print("\n-- Trigonometric Functions (Degrees) --")
        print("1. sin(x)\n2. cos(x)\n3. tan(x)")
    elif choice == 6:
        print("\n-- Angle Conversion --")
        print("1. Degree to Radian\n2. Radian to Degree")
    elif choice == 7:
        print("\n-- Number System Conversions --")
        print("1. Decimal to Binary/Octal/Hex\n2. Binary/Octal/Hex to Decimal")

# Main Loop
while True:
    show_main_menu()
    main_choice = int(input("Enter main choice: "))

    if main_choice == 0:
        print("Exiting calculator. Goodbye!")
        break

    if 1 <= main_choice <= 7:
        show_submenu(main_choice)
        sub_choice = int(input("Enter sub-function: "))

        if main_choice == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            ops = [add, subtract, multiply, divide, modulus]
            print("Result:", ops[sub_choice - 1](a, b))

        elif main_choice == 2:
            a = float(input("Enter the number: "))
            if sub_choice == 1:
                b = float(input("Enter the exponent: "))
                print("Result:", power(a, b))
            elif sub_choice == 2:
                print("Result:", square_root(a))

        elif main_choice == 3:
            a = float(input("Enter the number: "))
            if sub_choice == 1:
                print("Result:", factorial(a))
            elif sub_choice == 2:
                print("Result:", exponential(a))

        elif main_choice == 4:
            a = float(input("Enter the number: "))
            if sub_choice == 1:
                print("Result:", natural_log(a))
            elif sub_choice == 2:
                print("Result:", log_base_10(a))

        elif main_choice == 5:
            a = float(input("Enter angle in degrees: "))
            if sub_choice == 1:
                print("Result:", sin(a))
            elif sub_choice == 2:
                print("Result:", cos(a))
            elif sub_choice == 3:
                print("Result:", tan(a))

        elif main_choice == 6:
            a = float(input("Enter value: "))
            if sub_choice == 1:
                print("Radians:", deg_to_rad(a))
            elif sub_choice == 2:
                print("Degrees:", rad_to_deg(a))

        elif main_choice == 7:
            if sub_choice == 1:
                a = int(input("Enter decimal number: "))
                b, o, h = dec_to_other(a)
                print(f"Binary: {b}, Octal: {o}, Hex: {h}")
            elif sub_choice == 2:
                val = input("Enter value: ")
                base = int(input("Enter base (2/8/16): "))
                print("Decimal:", other_to_dec(val, base))
    else:
        print("Invalid main choice.")
