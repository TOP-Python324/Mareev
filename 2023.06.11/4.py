meaning_dict = {}
while (meaning := input("Введите ключ и значение: ")):
  meaning = meaning.split(" ")
  for i in range(len(meaning)):
      meaning_dict[int(meaning[i])] = meaning[i + 1]
      break
val = input("Введите значение: ")
for key, value in meaning_dict.items():
    if val == value:
        result = key
        break
    elif val not in meaning_dict.values():
        result = "! value error !"
print(result)

# Введите ключ и значение: 100 x
# Введите ключ и значение: 445 r
# Введите ключ и значение: 111 h
# Введите ключ и значение: 345 k
# Введите ключ и значение: 664 f
# Введите ключ и значение:
# Введите значение: h
# 111