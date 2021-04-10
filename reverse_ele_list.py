


# define a function that take list words as argument and 
# returen list with reverse of every element in that list

# ex : ['abc', 'tuv', 'xyz']  ------> ['cba', 'vut', 'zyx']

def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

words = ['abc', 'tuv', 'xyz']

print(reverse_elements(words))


