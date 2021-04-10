# program for search bigger in given three no:

def big_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
num1 = int(input("enter the first no: "))
num2 = int(input("enter the second no:"))
num3 = int(input("enter the third no:"))
print(big_num(num1,num2,num3))