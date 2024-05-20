def print_num(num):
    if num>0:
        print_num(num-1)
    print(num)

print_num(10)
