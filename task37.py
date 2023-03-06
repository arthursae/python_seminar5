# '37. Дано натуральное число *N* и последовательность из *N* элементов.
# Требуется вывести эту последовательность в обратном порядке.
#
# ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

number_n = int(input('Введите число N: '))


def descending_order(number_n):
    if number_n == 1:
        print(number_n, end=' ')
        return 1
    print(number_n, end=' ')
    return descending_order(number_n - 1)


descending_order(number_n)
