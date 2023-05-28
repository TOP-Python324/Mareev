mile_whole = int(input("Введите челую часть: "))
mile_fractional = int(input("Введите дробную часть: "))
mile = f"{mile_whole}.{mile_fractional}"
mile = float(mile)
const_km = 1.61
km = mile * const_km
print(f'{mile} миль = {km:.1f} км')

# Введите челую часть: 12
# Введите дробную часть: 6
# 12.6 миль = 20.3 км