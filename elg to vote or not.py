#write a program to input name and age and find elg to vote

name=input("enter your name")
age=int(input("enter your age"))
print(f'{name} is elg to vote') if age>=18 else print(f'{name}is not elg to vote')
