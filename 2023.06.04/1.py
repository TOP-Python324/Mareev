total = []
while number := int(input("Введите число: ")):
    if number % 7 != 0:
        break
    else:
        total.append(number)
print(*reversed(total))


# Введите число: 7
# Введите число: 14
# Введите число: 21
# Введите число: 28
# Введите число: 49
# Введите число: 56
# Введите число: 22
# 56 49 28 21 14 7


