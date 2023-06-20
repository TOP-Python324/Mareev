number1 = input().split(" ")
number2 = input().split(" ")
l1 = [int(el) for el in number1]
l2 = [int(el) for el in number2]
for i in range(0, len(l1)):
    if l1[i:i+len(l2)] == l2:
        print("Да")
        break
else:
        print("Нет")