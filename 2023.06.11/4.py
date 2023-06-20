meaning_dict = {}
while (meaning := input("Введите ключ и значение: ")):
  meaning = meaning.split(" ")
  for i in range(len(meaning)):
      meaning_dict[int(meaning[i])] = meaning[i + 1]
      print(meaning_dict)
      break
val = input("Введите значение: ")
for key, value in meaning_dict.items():
    if val == value:
        result = key
        break
    elif val not in meaning_dict.values():
        result = "! value error !"
print(result)
