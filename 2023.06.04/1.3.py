num = int(input("Ввелите число: "))
numbers = 0
for i in range(1, num + 1):
    if num % i == 0:
        numbers += i
print(numbers)

# Ввелите число: 64
# 127