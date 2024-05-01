#write a program to input name and 2 sub marks and find result (pass or fail)

name=input("enter any name")
sub1=int(input("enter sub1 marks"))
sub2=int(input("enter sub2 marks"))
result="pass" if sub1>=40 and sub2>=40 else "fail"
print(f'{name} result is {result}')
         
        
