year = int(input("Введите год:"))

if year % 4 == 0 and not(year % 100 == 0) or year % 400 == 0:
    print("Да")
else:
    print("Нет")
    
# Введите год:2023
# Нет