# '35. 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

def get_user_input(msg):
    n = int(input(msg))
    if n < 2:
        return get_user_input('Введите натуральное число больше 1: ')
    return n


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_rec(n):
    if n > 2 and number % (n - 1) == 0:
        return False
    elif n == 2:
        return True
    return is_prime_rec(n - 1)


number = get_user_input('Введите число: ')
n = number
print(is_prime_rec(n))
# print(is_prime(n))
