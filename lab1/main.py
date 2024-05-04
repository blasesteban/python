import collections
import math


def hello_world():
    print('Hello World!')


def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def greatest_common_divisor(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Operands a and b must be non-negative!")

    m = min(a, b)
    while m >= 1:
        if a % m == 0 and b % m == 0:
            return m
        m = m - 1


def print_triangle(n, p):
    i = 0
    while i < n:
        x = i * p + 1
        while x > 0:
            print('x', end="")
            x = x - 1
        print()
        i = i + 1


def money_rain():
    hundreds = int(input("Hundreds: "))
    two_hundreds = int(input("Two hundreds: "))
    five_hundreds = int(input("Five hundreds: "))
    print(hundreds * 100 + two_hundreds * 200 + five_hundreds * 500)


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def time_interval():
    start_hour = int(input("Start hour: "))
    start_minute = int(input("Start minute: "))
    start_second = int(input("Start second: "))
    end_hour = int(input("End hour: "))
    end_minute = int(input("End minute: "))
    end_second = int(input("End second: "))

    # print((end_hour - start_hour) * 60 * 60 +
    #       (end_minute - start_minute) * 60 +
    #       (end_second - start_second))
    start_time = start_hour * 60 * 60 + start_minute * 60 + start_second
    end_time = end_hour * 60 * 60 + end_minute * 60 + end_second
    if end_time - start_time < 0:
        print(end_time - start_time + 24 * 60 * 60)
    else:
        print(end_time - start_time)


def triangle(ax, ay, bx, by, cx, cy):
    a = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2)
    b = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    c = math.sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
    perimeter = a + b + c
    s = perimeter / 2
    tmp = 2 * math.sqrt(s * (s - a) * (s - b) * (s - c))
    h_a = tmp / a
    h_b = tmp / b
    h_c = tmp / c
    area = a * h_a / 2
    alpha = math.acos(((bx - ax) * (cx - ax) + (by - ay) * (cy - ay)) / (b * c))
    beta = math.acos(((ax - bx) * (cx - bx) + (ay - by) * (cy - by)) / (a * c))
    gamma = math.acos(((ax - cx) * (bx - cx) + (ay - cy) * (by - cy)) / (a * b))
    return a, b, c, perimeter, area, alpha, beta, gamma, alpha + beta + gamma, h_a, h_b, h_c


def square_numbers():
    n = int(input("Amount of first square numbers: "))
    x = 1
    while x <= n:
        print(x ** 2, end=", ")
        x = x + 1


def spheres():
    # n = 10
    # volume = 4 * math.pi * n ** 3 / 3
    # while volume < 1000000:
    #     print(n, volume)
    #     n = n + 10
    #     volume = 4 * math.pi * n ** 3 / 3

    n = 10
    while True:
        volume = 4 * math.pi * n ** 3 / 3
        if volume >= 1000000:
            break
        print(n, volume)
        n = n + 10


def pow(base, exponent):
    tmp = 1
    result = 1
    while tmp <= exponent:
        result = result * base
        tmp = tmp + 1
    print(result)


def my_sequence():
    n = int(input("n: "))
    x = 2
    i = 0
    while i < n:
        x = 2 * x + 5
        i = i + 1
    print(x)


def cubic_root(a, eps, ):
    x = a
    i = 0
    while math.fabs(x ** 3 - a) / a > eps:
        print(i, x, x ** 3)
        x = (a / x ** 2 + 2 * x) / 3
        i += 1
    print(i, x, x ** 3)


def divisors(n):
    i = 2
    if i < n:
        print(i, end="")
    i += 1
    while i < n:
        if n % i == 0:
            print(",", i, end="")
        i += 1


def all_numbers():
    i = 4
    while i <= 6:
        j = 4
        while j <= 6:
            k = 4
            while k <= 6:
                l = 4
                while l <= 6:
                    print(str(i) + str(j) + str(k) + str(l))
                    l += 1
                k += 1
            j += 1
        i += 1


def bus_tickets():
    i = 1
    while i < 10:
        j = i + 1
        while j < 10:
            k = j + 1
            while k < 10:
                print(i, j, k, sep="")
                k += 1
            j += 1
        i += 1


def increasing_intervals(a, b):
    i = 1
    x = a
    if x <= b:
        print(x, end="")
        x += i
        i += 1
    while x <= b:
        print(" " + str(x), end="")
        x += i
        i += 1


def A0_papersize(precision=2):
    x = math.sqrt(1 / math.sqrt(2)) * 1000
    y = math.sqrt(2) * x
    i = 0
    while i <= 6:
        print(f"A{i}: {round(x, precision)}x{round(y, precision)} mm")
        tmp = x
        x = y / 2
        y = tmp
        i += 1


def table(n, ):
    i = 0
    k = 1
    while i < n:
        j = 0
        while j < n:
            print(f"{k:>6},", end="")
            # k=i*n + j + 1
            j += 1
            k += 1
        print("")
        i += 1


def chest(n):
    i = 1
    if i <= n:
        j = 1
        if j <= n:
            print("+", end="")
            j += 1
        while j < n:
            print("-", end="")
            j += 1
        if j == n:
            print("+", end="")
        print("")
        i += 1
    while i < n:
        j = 1
        if j <= n:
            print("|", end="")
            j += 1
        while j < n:
            if i == j:
                print("\\", end="")
            else:
                print(" ", end="")
            j += 1
        if j == n:
            print("|", end="")
        print("")
        i += 1
    if i == n:
        j = 1
        if j <= n:
            print("+", end="")
            j += 1
        while j < n:
            print("-", end="")
            j += 1
        if j == n:
            print("+", end="")
        print("")


def roof(n):
    i = 1
    m = n * 2
    while i <= n:
        j = 1
        while j <= m:
            if n == j + i - 1:
                print("#", end="")
            elif n == m - (j - i):
                print("#", end="")
            else:
                print(" ", end="")
            j += 1
        print("")
        i += 1


def sinus(rad=2 * math.pi):
    degree = rad / math.pi * 180
    i = 0
    while i <= degree:
        k = 10 * (1 + math.sin(i * math.pi / 180))
        j = 1
        while j <= k:
            print(" ", end="")
            j += 1
        print("x")
        i += 20


def sinus2(end=2 * math.pi, width=20, height=10):
    i = 0
    while i < end / math.pi * height:
        j = round(math.sin(i * math.pi / height) * width + width)
        k = 1
        while k <= j:
            print(" ", end="")
            k += 1
        print("x", j)
        i += 1

if __name__ == '__main__':
    ...
    # hello_world()
    # print(quadratic(2, 5, -10))
    # print(greatest_common_divisor(8, 12))
    # print(money_rain())
    # print(celsius_to_fahrenheit(5))
    # print_triangle(7, 2)
    # time_interval()
    # print(triangle(0, 0, 4, 0, 0, 3))
    # square_numbers()
    # spheres()
    # pow(5, 0)
    # my_sequence()
    # cubic_root(27, 0.001,)
    # divisors(60)
    # all_numbers()
    # bus_tickets()
    # increasing_intervals(4, 25)
    # A0_papersize()
    # table(10)
    # chest(1)
    # roof(6)
    # sinus2(end=2 * math.pi, 10)
    # for p in [0,1]:
    #     for q in [0,1]:
    #         print(p,q, p + q != 0, bool(p) or bool(q) )
    #         print(p, q, p * q != 0, bool(p) and bool(q))
    #         print()

