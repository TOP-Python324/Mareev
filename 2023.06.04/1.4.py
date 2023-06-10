n = int(input("Введите количество разрядов: "))
lst=[]
for i in range(2, n+1):
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print(len(lst))

# Введите количество разрядов: 21
# 8
