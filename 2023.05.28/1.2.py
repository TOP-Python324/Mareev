number_1 = int(input("Введите первое число:"))
number_2 = int(input("Введите второе число:"))

if number_1 % number_2 == 0:
    print(f'{number_1} делится на {number_2} нацело \n '
          f'частное: {int(number_1 / number_2)}')
else:
    print(f'{number_1} не делится на {number_2} нацело \n'
          f'неполное частное:{number_1 // number_2} \n'
          f'остаток: {number_1 % number_2}')

# Введите первое число:9
# Введите второе число:3
# 9 делится на 3 нацело
 # частное: 3
