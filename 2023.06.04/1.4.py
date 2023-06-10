n = int(input("Введите количество разрядов: "))
num = "9" * n
lst = []
for i in range(2, int(num)):
    for j in range(2, i):
        if i % j == 0:
            break
        elif len(str(i)) != n:
            break
    else:
     lst.append((i))
if n > 1:
    lst.remove(2)
print(len(lst))

# Введите количество разрядов: 4
# 1061