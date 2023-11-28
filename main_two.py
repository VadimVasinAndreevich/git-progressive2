def math_operation(a, b):
    x = a + b
    y = a - b
    return x, y


number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
print(math_operation(number_one, number_two))