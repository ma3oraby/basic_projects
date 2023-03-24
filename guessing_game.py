print ("Welcome to The Programming Languages name Guessing Game")

correct_guess = "python"
player_guess = ""
guesses_count = 0 
guesses_limit = 3
out_of_guesses = False 

while player_guess != correct_guess and not out_of_guesses : 
    if guesses_count < guesses_limit :
        player_guess = input ("plz enter your guess : ")
        guesses_count += 1 

    else : 
        out_of_guesses = True 

if out_of_guesses : 
    print ("YOU Lose")

else : 
    print ("You Win :)")