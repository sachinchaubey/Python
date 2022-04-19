# pass statement
#x = 12
#if x > 12:
#    pass
###########################
#if else statement
#age = int (input("enter you age :"))
#if age >= 13:
#     print("you are above 13")
#else:
#    print("sorry, you can't ")
##############################


# chapter 3: Exercise 1: if else
# Number guessing game
# Exerxise solution

#winning_number = 34;

#user_number = int (input("enter any number between 1 to 100 to win number gussing game :"))
#if winning_number == user_number:
 #   print("user are win")
# else:
#    if user_number < winning_number:  nasted if-else condition 
 #       print("too low ")
 #   else:
 #       print("too high")

 #####################################

# AND , OR Operator:
# check two condition at same time
# and, or
#name = 'abc'
#age = 15
#if name == 'abc' or age == 12:
#    print("condition true")
#else:
#    print("condition false")

###################################

#Chapter 3: Exercise 2: and ,or operator
#EXERCISE -WATCH POCO

#name = input("enter your name :")
#age = int(input("enter your age :"))
#if (name[0] == 'a' or name[0] == 'A') and age >= 10:
#    print("you watch poco movies")
#else:
#    print("sorry")

#########################################

#if-elif-else statement:(for check multiple statement)
#| problem:
#show ticket pricing
# 0 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# abpve 60 (300)
'''
age =int(input("please input your age :"))
if age<= 0:
    print("you can't watch")
elif 0<age<=3:
    print("ticket price : Free")
elif 3<age<=10:
    print("ticket price :150")
elif 10<age<=60:
    print("ticket price :250")
else:
    print("ticket price :300")'''

 ####################################

 #in keyword
 #if with in
'''
 name = "sachin"
if 'a' in name:
    print("a is present")
else:
    print("a is not present")'''


#####################################
'''
#check empty or not
# important
name = "acb"
if name:    #true if string is not empty
    print("string is not empty")
else:
    print("string is empty")
'''
###########################################

#while loop, for loop
'''
i = 1
while i<=10:
   print("hello world")
   i += 1 '''

##############################################
'''
# sum : 1 to 10 uses while loop
k = 0
i = 1
n = int(input("enter the no :"))
while i <= n:
    
   k += i
   i += 1
print(k)'''


##############################
'''
num = input("enter the number more the 1 digits :")

total = 0
i = 0
while i < len(num):
    total += int(num[i])
    i += 1
print(total)'''

###################################
 
'''
a = 1
b = 2
c = a+b
print(c)'''

#############################################
'''
name = input("enter the name :")
temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
'''
 
 #######################################
 
#for loop with range function :

'''
for i in range(7, 11):
    print(f"hello world :{i}")
'''

#################################################

#for loop example :
#sum from 1 to 10 using for loop
'''
n = int(input("enter the num :"))
total = 0
for i in range(0,n+1):
    total += i
print(total)'''
#######################################
'''
total = 0
num = input("enter the number")
for i in range(0 , len(num)):
    total += int(num[i])
print(total)'''

###########################################
'''
name = input("enter your name :")
temp = ""
for i in range(0, len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")'''
        
######################################################
'''
#break and continue keyword :
for i in range(0,11):
    if i == 5:
       # break  # for if 5 is come the break loop and out of the loop
       continue # for if 5 is come then contunue statement is work and not print 5 means left 5 : 
    print(i)'''

#########################################################
#  number gussing game
'''
#winning_num = 43
import random
winning_num = random.randint(1,100)
guess = 1
number = int(input("guess a number between 1 and 100 :"))
game_over = False

while not game_over:
    if number == winning_num:
        print(f"you win, and you guessed this number in {guess} time ")
        game_over = True
    else:
        if number < winning_num:
            print("too low")
            #guess += 1
            #number = int(input("guess again :"))
        else:
            print("too high")
        guess += 1
        number = int(input("guess again :"))
     #DRY - don't reapet youself  ''' 
##############################################################

# Step argument in range function :
 
#for i in range(1,11,2):   # where 2 is range means 2 no over step
 #   print(

######################################################################

# For loop and string:
'''
name = "sachin"
for i in range(len(name)):
    print(name[i])'''
'''
name = "sachin"
for i in "sachin":
    print(i)'''

'''
# sum of 2 digit using for
num = input("enter a num :")
total = 0
for i in num:
    total += int(i)
print(total)'''


#######################################################################
########################################################################
########################################################################
########################################################################

# Chap 4:
'''
# Functins: we use def for calling function in python:

def add(a,b):
    return a+b
#print(add(4,6))

#if we are given a string then -

first_name = input("enter first name :")
last_name = input("enter last name :")
print(add(first_name,last_name))'''

###############################################################
'''
# Print VS return :

def add(a,b,c):
    return a+b+c
# here return are not important here we are normally printe replace return : both are same 
print(add(5,5,5))'''

###########################################################################

# practice functin :
#ex -1
'''
def last_char(name):
    return name[-1]

print(last_char("sachin"))'''
# you can't use any no bcz error produce bcz subscriptin

#ex - 2
'''
def even_odd(num):
    if num%2 == 0:
        return "even"
    return "odd"
r = even_odd(7)
print(r)'''

#ex -2
'''
def is_even(num):
    return num%2 == 0  #true
    #if num%2 == 0:
       # return True
    #return False
   
print(is_even(19))'''

#ex-3
'''
def song():
    return "happy birthday"
print(song())'''

#########################################################
# Chapter 4 : exersice 1 : experiment big num b/w two no>
'''
def big_num(num1,num2):
    if num1 > num2:
        return num1
    return num2
x = int(input("enter the first num :"))
y = int(input("enter the second no:"))
print(big_num(x,y))'''

##########################################################

# chapter 4 : exersice 2 : experiment big no. between three no:
'''
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
print(big_num(num1,num2,num3))'''

###########################################

#function inside function:
'''
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
'''

#########################################################################

# chapter 4: Exersice 3 : define is_palindrome function take one word is string as input and return True if it is palindrome else return FAlse
'''
def is_palindrome(name):
    #reversed_name = name[::-1]    #wey 1
    #if name == reversed_name:     #wey 2
    #return name == word[::-1]     #wey 3
    if name == name[::-1]:         #way 4
        return True
    return False

name = input("Enter the palindrome word :")
print(is_palindrome(name))'''

######################################################################
'''
# Fibonacci series:

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
Fibonacci_seq(n)'''

####################################################
#################################################################
#############################################################
############################################################
#############################################################
'''
# CHAPTER 5 : 
# list

number = [1,3,4]
print(number)

word = ["wprd","word"]
print(word)

mixed = [1,2,5,"word",2.4,None]
print(mixed)'''

###############################################################

'''
# some functions of list

num = [1,4,3,5,2]
#print(sorted(num))
#num.clear()
#num_copy = num.copy()
print(num)

'''


###################################################
'''
# compare lists : == , is

fruits =["apple","kiwi","orange"]
fruits1 =["apple","kiwi","orange"]
print(fruits == fruits1)
print(fruits is fruits1)'''

#############################################

# join and split method:
'''
#' split method: it is comvert string to list
user_info = 'sachin 34'.split()
print(user_info)'''

# join method : it is convert list to string 
''' 
user = ['Sachin', '24']
print(','.join(user))'''

#######################################################
# loops in list;
'''
fruits = ['orange','apple','pear','banana']
for i in fruits:
    print(i)
'''

#####################################33333333333333333
# List inside list:
'''
matrix = [[1,[2,3]],[4,[5,6]],[7,[8,9]]]
#print(matrix[0])
for sublist in matrix:
    for i in sublist:
            print(i)
print(type(matrix))
'''
###############################################
'''
num = list(range(1,11))
print(num)'''

#########################################################

# Chapter 5: Exersice 1:
'''
#num = list(range(int(input("enter the no. :")))

def square_list(l):
    square =[]
    for i in l:
        square.append(i**2)
    return square

num = list(range(1,11))
print(num)
print(square_list(num))
'''

################################################

# exersice : 2
# reversed list print:
'''
def reversed_list(l):
    reversed = []
    for i in range(len(l)):
        
        reversed.append(l.pop())
    return reversed
    #pop.reversed_list()

num = list(range(0,11))
print(reversed_list(num))
'''

##############################################

# exersice : 5.3
'''

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
'''

#################################################

# eCERSICE : 5.4
'''
# FILTTER : ODD AND EVEN AND RETURN:

def filter_odd_even(l):
    odd_nums = []
    even_nums = []
    for i in l:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums,even_nums]
    return output

nums = [1,2,3,4,5,6,7]
print(filter_odd_even(nums))
'''

################################################################
'''
f1 = ['sachin', 'shivam', 'rishav']
f2 = ['utkarsh','gaurav', 'pratik']

f1.extend(f2)
print(f1)
'''
#################################################################

# EXERSICE : 5.5:
'''
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
'''

############################################################
'''
# min and max functins:
numbers = [6,33,66]
print(min(numbers))
print(max(numbers)) 
def gretest_(l):
    return max(l) - min(l)
print(gretest_(numbers))
'''

#############################################################

# EXERSICE : 5.6:
 
# def sublist_counter(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count
# mixed = [2,3,5,[4,4],[5,6]]
# print(sublist_counter(mixed))

######################################################################
##############################################################################
##############################################################################
##############################################################################
###############################################################################
#############################################################################


# Tuple :
'''
example = (2,4,5,6)
print(example[1:3])
'''
'''
mydata = raw_input('Prompt :')
print (mydata)
'''
'''
f1,f2,f3 = input("enter the three no :").split(',')
avg = (int(f1) + int(f2) + int(f3))/3
print(f"sum are :{round(avg,
'''
'''
ab = [100,2,3,4,5]
print(ab[::-1])
'''
'''
list1 = ['m','n']
list2 = ['y','k']
for i in len(list1):
    for j in len(list2):
        print(list[i]+list[j])
'''
'''
r = [1,3,4,5,6,7,8]
square= []
for i in r:
    square.append(i*i)
print (square)
'''

    


'''
list1 = ['1','2','3']
print(len(list1))
'''

'''
list1 = ['Mike','','Emma','','kelly']
r = list(filter(None,list1))
print(r)'''
'''
list1 = [10,20,[300,400,[5000,6000],500],30,40]
'''

#looping in tuples
#mixed =(1,2,3,4.0)
# for i in mixed:
#     print(i)


# max = ('sachin','chaubey',['utkarsh','yadav'])
# max[2].pop()
# max[2].append('shivam')
# print(max)

# def mix(int1,int2):
#      add = int1 + int2
#      multiply = int1*int2
#      return add, multiply
# print(mix(2,3))

#mix = (1,3,5,6)
# #num = str([1,2,3])
# print(num)
# print(type(num))

#############################################
############################################
#dictoniries

# mix = {
#     'name' : 'sachin',
#     'age' : 21,
#     'fav_movies' : ['bhagmbhab','avangers'],
#     'fav-song' : ['thunder','mast_magen'],
# }
# print(mix[])

# user ={}
# user['name'] ='sachin'
# print(user)

 






   