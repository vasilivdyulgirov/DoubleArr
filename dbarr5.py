# Въвеждане на размерите (матрицата е квадратна)
n = int(input("Въведи размер на квадратната матрица (n): "))

# Въвеждане на елементите на матрицата
array = []
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"array[{i}][{j}] = "))
        row.append(value)
    array.append(row)

# Извеждане на матрицата
print("\nВъведената матрица е:")
for row in array:
    for el in row:
        print(f"{el:>6}", end=" ")
    print()

# 1. Произведение на елементите по главния диагонал
mult = 1
for i in range(n):
    mult *= array[i][i]
print(f"\nПроизведение по главния диагонал: {mult}")

# 2. Максимален елемент над главния диагонал (i < j)
max_above = array[0][1]  # започваме от първия елемент над диагонала
for i in range(n - 1):
    for j in range(i + 1, n):
        if array[i][j] > max_above:
            max_above = array[i][j]
print(f"Максимум над главния диагонал: {max_above}")

# 3. Сума на четните елементи под главния диагонал (i > j)
sum_below = 0
for i in range(1, n):
    for j in range(i):
        if array[i][j] % 2 == 0:
            sum_below += array[i][j]
print(f"Сума на четните под главния диагонал: {sum_below}")
