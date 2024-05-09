#write a program to read marks of m students and n subjects
#calculate total avg,result

m=int(input("how many student"))
n=int(input("how many subject"))
stud=[]

for i in range(m):
    row=[]
    for j in range(n):
        marks=int(input("enter msrks"))
        row.append(marks)
    stud.append(row)

for i in range(m):
    total=sum(stud[i])
    avg=total/n
    result="pass"
    for j in range(n):
        if stud[i][j]<40:
            result="fail"
            break
    print(f'{stud[i]}\t{total}\t{avg:.2f}\t{result}')
