# Въвеждане на брой редове и колони
rows = int(input("Въведи брой редове: "))
columns = int(input("Въведи брой колони: "))

# Създаване на празен двумерен масив
arr = []

# Въвеждане на елементите
for i in range(rows):
    row = []
    for j in range(columns):
        value = float(input(f"arr[{i}][{j}] = "))
        row.append(value)
    arr.append(row)
print("Матрицата е:")
for i in range(rows):
    for j in range(columns):
        print(f"{arr[i][j]:>6}", end=" ")
    print()  # нов ред след всеки ред от матрицата
