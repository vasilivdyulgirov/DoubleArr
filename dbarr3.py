# Въвеждане на размерите
n = int(input("Въведи брой редове: "))
m = int(input("Въведи брой колони: "))

# Въвеждане на елементите на масива
mas = []
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"mas[{i}][{j}] = "))
        row.append(value)
    mas.append(row)

# Извеждане на масива във вид на таблица
print("\nМатрицата е:")
for row in mas:
    for el in row:
        print(f"{el:>6}", end=" ")
    print()

# Изчисляване на произведението на четните елементи по колони
print("\nПроизведение на четните елементи по колони:")
for j in range(m):
    mult = 1
    has_even = False
    for i in range(n):
        if mas[i][j] % 2 == 0:
            mult *= mas[i][j]
            has_even = True
    if has_even:
        print(f"{mult:>6}", end=" ")
    else:
        print(f"{'-':>6}", end=" ")
print()
