# ИСПРАВИТЬ: речь опять об одной фигуре
figure_1 = input("Введите координаты первой фигуры:")
figure_2 = input("Введите координаты второй фигуры:")

x_1 = int(figure_1[1])
y_1 = ord(figure_1[0]) - 96
x_2 = int(figure_2[1])
y_2 = ord(figure_2[0]) - 96

# ИСПРАВИТЬ: в правом операнде and не хватает сравнения, в итоге получаете невозможный ход (см. пример ниже)
if abs(x_1 - x_2) <= 1 and abs(y_1 - y_2):
    print("да")
else:
    print('нет')


# Введите координаты первой фигуры:d3
# Введите координаты второй фигуры:e4
# да

# Введите координаты первой фигуры:a1
# Введите координаты второй фигуры:d1
# КОММЕНТАРИЙ: король верхом на ладье?
# да


# ИТОГ: хорошо, доработать — 3/5
