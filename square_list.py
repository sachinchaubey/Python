#program for square of a list:


def square_list(l):   # this one is a function.
    square =[]
    for i in l:
        square.append(i**2)
    return square

num = list(range(1,11))  # enter the list by the input
print(num)               # print the list those are given by the programmer ,, this one is optional

print(square_list(num))  # this is the output
