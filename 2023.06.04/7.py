symbol = '.,:;!?–—\'\"()*/'
# ПЕРЕИМЕНОВАТЬ: символ строки — character, char, ch
text_ls = [el for el in input("Введите текст: ") if el not in symbol]
text_str = "".join(text_ls)
print(text_str)


# Введите текст: На свете не бывает ошибочных мнений. Бывают мнения, которые не совпадают с нашими, вот и всё.
# На свете не бывает ошибочных мнений Бывают мнения которые не совпадают с нашими вот и всё


# ИТОГ: отлично — 3/3
