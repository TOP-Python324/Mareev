fib1 = fib2 = 1

number = int(input("Введите число: "))

# ИСПРАВИТЬ: если пользователь введёт 1, то и должно быть выведено одно число последовательности — это даже в примере показано
print(fib1, fib2, end=' ')

# ПЕРЕИМЕНОВАТЬ: когда переменная цикла не используется, то её заменяют символом _
for i in range(2, number):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')


# Введите число: 14
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Введите число: 1
# 1 1


# ИТОГ: доработать — 3/5
