text = []
while (fruits := input("Введите фрукт: ")):
    text.append(fruits)
print(*text[:-2], " и ".join(text[-2:]), sep=", ")

