scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
result = 0
text = input("Введите слово: ").upper()
for key, value in scores_letters.items():
    for el in text:
        if el in value:
            result += key
print(result)

# Введите слово: полиформизм
# 26