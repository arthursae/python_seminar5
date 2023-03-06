# '31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

def fibonachi(number_n):
    if number_n == 1:
        return 1
    elif number_n == 0:
        return 0
    else:
        return fibonachi(number_n - 2) + fibonachi(number_n - 1)

n = 12
print(fibonachi(n))

