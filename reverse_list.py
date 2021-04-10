# printf reverse of a list: using pop and append method:

def reversed_list(l):
    reversed = []
    for i in range(len(l)):
        
        reversed.append(l.pop())
    return reversed
    #

num = list(range(0,11))
print(reversed_list(num))
