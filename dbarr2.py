# Въвеждане на размерите
n = int(input("Въведи брой редове: "))
m = int(input("Въведи брой колони: "))

# Създаване на двумерен масив
arr = []

# Въвеждане на елементите
for i in range(n):
    row = []
    for j in range(m):
        value = float(input(f"arr[{i}][{j}] = "))
        row.append(value)
    arr.append(row)

# Извеждане на масива с изчисляване на сумата за всеки ред
print("\nМатрицата със сумите на редовете:")
for i in range(n):
    row_sum = 0
    for j in range(m):
        print(f"{arr[i][j]:>6}", end=" ")
        row_sum += arr[i][j]
    print(f" | Сума: {row_sum}")
