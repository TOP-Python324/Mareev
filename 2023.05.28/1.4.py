figure_1 = input("Введите координаты первой фигуры:")
figure_2 = input("Введите координаты второй фигуры:")

black_cells = ['a1', 'c1', 'e1', 'g1', 'b2', 'd2', 'f2', 'h2', 'a3',
               'c3', 'e3', 'g3', 'b4', 'd4', 'f4', 'h4', 'a5', 'c5', 'e5', 'g5', 'b6',
               'd6', 'f6', 'h6', 'a7', 'c7', 'e7', 'g7', 'b8', 'd8', 'f8', 'h8']

white_cells = ['b1', 'd1', 'f1', 'h1', 'a2', 'c2', 'e2', 'g2', 'b3', 'd3', 'f3', 'h3',
               'a4', 'c4', 'e4', 'g4', 'b5', 'd5', 'f5', 'h5', 'a6', 'c6', 'e6', 'g6',
               'b7', 'd7', 'f7', 'h7', 'a8', 'c8', 'e8', 'g8']

if figure_1 in black_cells and figure_2 in black_cells :
    print("Да")
elif figure_1 in white_cells and figure_2 in white_cells:
    print("Да")
else:
    print("Нет")
    
# Введите координаты первой фигуры:b2
# Введите координаты второй фигуры:c3
# Да
