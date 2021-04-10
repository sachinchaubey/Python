

# COMMON ELMENTS FINDER FUNCTION IN TWO INPUT LIST:

def common_finder(l1,l2):
    output = []     # make a empty output var where common elements are assinged
    for i in l1:
        if i in l2:
            output.append(i)
    return output

num1 =[1,2,3,4,5]    # list no 1
num2 =[1,2,8,7,4]    # list no 2

print(common_finder(num1,num2))   # function are calling
