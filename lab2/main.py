from lab1.main import greatest_common_divisor


def check_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        print("not triangle")
    elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
        print("it is a right angle triangle")
    else:
        print("it is just a normal triangle")


def lesser_greater_equal(a, b, c):
    # def get_key(it):
    #     return it[1]

    items = [('a', a), ('b', b), ('c', c)]
    items.sort(key=lambda it: it[1])

    # items.sort(key=get_key)

    def get_relation(x, y):
        if x < y:
            rel = '<'
        else:
            rel = '='
        return rel

    for i in range(len(items) - 1):
        print(items[i][0], get_relation(items[i][1], items[i + 1][1]), sep='', end='')
    print(items[-1][0])


def char_type(char):
    if 122 >= ord(char) >= 97:
        print('it is a low case letter')
    elif 90 >= ord(char) >= 65:
        print('It is a capital letter')
    elif 57 >= ord(char) >= 48:
        print('it is a number')
    else:
        print('it is a special character')


def caesar_code(text):
    new_text = ""
    for i in range(len(text)):
        if text[i] == "z":
            new_text += "a"
        elif text[i] == "Z":
            new_text += "A"
        else:
            new_text += chr(ord(text[i]) + 1)
    print(new_text)


def bird_language(text):
    new_text = ""
    for i in range(len(text)):
        if text[i] in 'aeiou':
            new_text += text[i] + 'v' + text[i]
        else:
            new_text += text[i]
    print(new_text)


def exam_score(points):
    grade = 0
    if points <= 23:
        grade = 1
    elif points <= 32:
        grade = 2
    elif points <= 41:
        grade = 3
    elif points <= 50:
        grade = 4
    elif points <= 60:
        grade = 5
    print(grade)


def euler_task():
    total_animal = 100
    total_money = 600
    pig_price = 21
    goat_price = 8
    sheep_price = 3
    pig_number = 0
    while pig_number <= total_animal:
        goat_number = 0
        while pig_number + goat_number <= total_animal:
            sheep_number = total_animal - goat_number - pig_number
            if pig_price * pig_number + goat_price * goat_number + sheep_price * sheep_number == total_money:
                print("pigs: ", pig_number, ", goats: ", goat_number, ", sheep: ", sheep_number, sep="")
            goat_number += 1
        pig_number += 1


def backwards(number):
    for i in range(len(str(number)) - 1, -1, -1):
        print(str(number)[i], end='')
    print()


def divisor_of_fivedigit_numbers():
    for i in range(10000, 100000, 1):
        if i % (i // 1000) == 0:
            print(i)


def fast_pow(base, exponent, should_print=True):
    if exponent == 1:
        result = base
    elif exponent % 2 == 0:
        result = fast_pow(base * base, exponent // 2, should_print=False)
    else:
        result = base * fast_pow(base, exponent - 1, should_print=False)
    if should_print:
        print(result)
    return result


def sum_of_fractions(a, b):
    gcd = greatest_common_divisor(a[1], b[1])
    print(f"The result is {int(a[0] * b[1] / gcd + b[0] * a[1] / gcd)}/{int(a[1] * b[1] / gcd)}")


def overlapping_quadrilaterals(board_num, cell_width, cell_height, column_count, row_count, x_offset, y_offset):
    width = cell_width * column_count
    height = cell_height * row_count
    total_width = width + (board_num - 1) * x_offset
    total_height = height + (board_num - 1) * y_offset
    i = 0
    while i < total_height:
        j = 0
        while j < total_width:
            k = board_num - 1
            found = False
            while k >= 0:
                if k * x_offset <= j < k * x_offset + width and k * y_offset <= i < k * y_offset + height:
                    if (((j - k * x_offset) // cell_width) % 2 == 0 and (
                            (i - k * y_offset) // cell_height) % 2 == 0) or (
                            ((j - k * x_offset) // cell_width) % 2 != 0 and (
                            (i - k * y_offset) // cell_height) % 2 != 0):
                        print('x', end='')
                    else:
                        print(k, end='')
                    found = True
                    break
                k -= 1
            if not found:
                print(' ', end='')
            j += 1
        print()
        i += 1


def chessboards(board_num, cell_size, cell_num, x_offset, y_offset):
    total_width = cell_size * cell_num + (board_num - 1) * x_offset
    total_height = cell_size * cell_num + (board_num - 1) * y_offset


def greatest_least():
    number = int(input('Give me a number: '))
    minimum = number
    maximum = number
    avr = number
    i = 1
    is_equal_to_zero = False
    while not is_equal_to_zero:
        number = int(input('Give me a number: '))
        if number == 0:
            is_equal_to_zero = True
            break
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
        avr = (avr * i + number) / (i + 1)
        i += 1
    print('minimum: ', minimum, ', maximum: ', maximum, ', average: ', avr, sep=' ')


def square_num(num):
    i = 1
    is_square_num = False
    while i <= num:
        if i * i == num:
            is_square_num = True
        i += 1
    print('is it a square number? ', is_square_num)


def num_of_divisors(num):
    result = 0
    i = 1
    while i <= num:
        if num % i == 0:
            result += 1
        i += 1
    print(result)


def sum_of_divisors(num):
    result = 0
    i = 1
    while i < num:
        if num % i == 0:
            result += i
        i += 1
    print(result)


def interval_with_prime_numbers(first, second):
    if first > second:
        i = first
        first = second
        second = i
    while first < second:
        divisors = 0
        j = 1
        while j <= first:
            if first % j == 0:
                divisors += 1
            j += 1
        if divisors == 2:
            print(first, end=', ')
        first += 1


def serial_of_sums_of_multiplications(num):
    result = 0
    i = 0
    while i <= num:
        result += i * (i + 1)
        i += 1
    print(result)


def euler_number(precision=20):
    i = 0
    result = 0
    while i < precision:
        divisor = 1
        j = 1
        while j <= i:
            divisor *= j
            j += 1
        result += 1 / divisor
        i += 1
    print(result)


def stars_between_nums(num1, num2):
    if num1 > num2:
        i = num1
        num1 = num2
        num2 = i
    sum = 0
    num1 += 1
    while num1 < num2:
        if num1 % 10 == 0:
            sum += num1
        num1 += 1
    i = 0
    while i < sum:
        print('*', end='')
        i += 1
    print('')


if __name__ == '__main__':
    ...
    # check_triangle(3, 4, 5)
    # check_triangle(3, 4, 7)
    # check_triangle(3, 4, 6)
    # caesar_code("azaz")
    # bird_language('pulykakakas')
    # exam_score(50)
    # lesser_greater_equal(2, 6, 4)
    # lesser_greater_equal(2, 4, 6)
    # lesser_greater_equal(6, 6, 4)
    # char_type('a')
    # char_type('A')
    # char_type('0')
    # char_type('?')
    # euler_task()
    # backwards(98765)
    # divisor_of_fivedigit_numbers()
    # fast_pow(2, 7)
    # sum_of_fractions((1, 2), (3, 4))
    # overlapping_quadrilaterals(4, 2, 3, 6, 4, 2, 3)
    # greatest_least()
    # square_num(81)
    # square_num(82)
    # num_of_divisors(12)
    # sum_of_divisors(12)
    # interval_with_prime_numbers(18, 0)
    # serial_of_sums_of_multiplications(6)
    # euler_number()
    stars_between_nums(10, 40)
