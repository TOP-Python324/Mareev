text = []
while (fruits := input("Введите фрукт: ")):
    text.append(fruits)
print(*text[:-2], " и ".join(text[-2:]), sep=", ")

# Введите фрукт: Груша
# Введите фрукт: Аппельсин
# Введите фрукт: Банан
# Введите фрукт: Яблоко
# Введите фрукт:
# Груша, Аппельсин, Банан и Яблоко