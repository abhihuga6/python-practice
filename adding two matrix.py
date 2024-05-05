#adding two matrix


m=int(input("enter how many rows"))
n=int(input("enter how many cols"))

matrix1=[]
matrix2=[]
matrix3=[]


print("enter elements of first matrix")
for i in range(m):
    row=[]
    for j in range(n):
        value=int(input("enter any value"))
        row.append(value)
    matrix1.append(row)
print("enter element of second matrix")
for i in range(m):
    row=[]
    for j in range(n):
        value=int(input("enter any value"))
        row.append(value)
    matrix2.append(row)

for i in range(m):
    row=[]
    for j in range(n):
        row.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(row)

print(matrix1)
print(matrix2)
print(matrix3)
