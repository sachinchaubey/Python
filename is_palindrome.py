#program for check the word is palindrome or not. (palindrome means a word which reverse and nonreverse both are same)



def is_palindrome(name):
    # this program is made by 4 and more way. so don't confiuse what is done by my in below 
    #reversed_name = name[::-1]    #wey 1
    #if name == reversed_name:     #wey 2
    #return name == word[::-1]     #wey 3
    if name == name[::-1]:         #way 4
        return True
    return False

name = input("Enter the palindrome word :")
print(is_palindrome(name))