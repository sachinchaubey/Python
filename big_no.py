#program for chose how is bigger between two no:

def big_num(num1,num2):
    if num1 > num2:
        return num1
    return num2
x = int(input("enter the first num :"))
y = int(input("enter the second no:"))
print(big_num(x,y))