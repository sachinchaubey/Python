#Create number guessing game :

#winning_num = 43   #43 is a any random number which are assign in a winning_num variable
import random  #this is a typw of module where no. are random generate by the program.
winning_num = random.randint(1,100) 
guess = 1      #guess is a var which are define how many time user take to guess the winning_num
user_input = int(input("enter any number b/w 1 to 100 :"))    # take input from the user 
game_over = False     # game_over is a var where False is assign. 

while not game_over:    
    if user_input == winning_num:
        print(f"you win,and you attempt {guess} times")
        game_over = True
    else:
        if user_input < winning_num:
            print("too low")
            guess += 1
            user_input = int(input("Guess again :"))
        else:
            user_input > winning_num
            print("too high")
            guess += 1
            user_input = int(input("Guess again :"))
            