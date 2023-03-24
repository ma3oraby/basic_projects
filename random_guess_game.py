#importing random module
import random 

#take input from user and check if it grater than zero or a number 
range_top = input ("Enter a number : ")
if range_top.isdigit():
    range_top = int (range_top)
    if range_top <= 0 : 
        print ("plz enter number greater than 0 next time ")
        quit()
else : 
    print ("plz enter a number only ")
    quit()

#make a random gues with random module 
random_number = random.randint (0,range_top)

gueses = 0 

#game loop 
while True :
    gueses += 1 #increase user guess every try to get the correct gues
    user_gues = input ("make a guess : ") #take a guess from user

    #check user gues 
    if user_gues.isdigit() : 
        user_gues = int(user_gues)
    
    else : 
        print ("plz enter a number")
        continue

    if user_gues == random_number : 
        print ("Congrats .. You got it :)")
        break 
    elif user_gues > random_number : 
        print ("You were above the correct gues")
    else : 
        print ("You were below the correct gues")

print (f"You got it in {gueses} guesses")