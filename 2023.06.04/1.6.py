numbers = [int(i) for i in input("Введите номер билета: ")]
if sum(numbers[0:3]) == sum(numbers[3:6]):
    print("Да")
else:
    print("Нет")
    
# Введите номер билета: 123321
# Да
