# program for define bigger no. between three no using function in function 

def big_number(num1,num2):
    if num1 > num2:
        return num1
    return num2

def big_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

#using function in function below    
def new_big_num(num1,num2,num3):
    bigger = big_number(num1,num2)
    return big_number(bigger,num3)

num1 = int(input("enter the first no: "))
num2 = int(input("enter the second no:"))
num3 = int(input("enter the third no:"))
print(new_big_num(num1,num2,num3))

