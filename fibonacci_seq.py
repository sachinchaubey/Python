# program for print fibonacci seq:


def Fibonacci_seq(n):
    a = 0 #first number
    b = 1 # seconde number
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)  # a b ,0 1
    else:
        print(a,b, end = " ")   # for print in horizental
        for i in range(n-2):
            c = a+b   
            a = b
            b = c
            print(b , end = " ") 

n = int(input("enter the number :"))
Fibonacci_seq(n)

