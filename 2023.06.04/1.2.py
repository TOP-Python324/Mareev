numbers = int(input("Введите количество чисел: "))
result = 0
for i in range(numbers):
    result += (number := int(input("Введите число: ")))
print(result)

# Введите количество чисел: 4
# Введите число: 2
# Введите число: 6
# Введите число: -4
# Введите число: 9
# 13