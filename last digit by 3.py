#write a program to find input number last digit is divisible with 3

num=int(input("anter any number"))
dig=num%10
print(f'{num}is dividible with 3')if dig%3==0 else print(f'{num} is not divisible with 3')
