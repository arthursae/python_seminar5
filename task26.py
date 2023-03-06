# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def raise_number_to_power(number, power):
    if power == 1:
        return number
    number *= num
    return raise_number_to_power(number, power - 1)


number = int(input('Введите число А: '))
power = int(input('Введите число B: '))
num = number
result = raise_number_to_power(number, power)
print(result)
