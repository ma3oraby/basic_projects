
#questions game
playing = input ('''Welcome to my Game ..
Do you want to play ? ''') 

if playing.lower () != 'yes' : 
    print ('Good bye ... ')
    quit () 
print ("OK , Let's play ..") 
score = 0 
questions = 0 

questions += 1
answer = input ('what is CPU stands for ? ') 
if answer.lower () == 'central processing unit' : 
    print ('correct answer')
    score += 1

else : 
    print ('wrong answer') 

questions += 1
answer = input ('what is HDD stands for ? ') 
if answer.lower () == 'hard disk drive' : 
    print ('correct answer')
    score += 1

else : 
    print ('wrong answer') 

questions += 1
answer = input ('what is RAM stands for ? ') 
if answer.lower () == 'random access memory' : 
    print ('correct answer')
    score += 1

else : 
    print ('wrong answer') 

questions += 1
answer = input ('what is SSD stands for ? ') 
if answer.lower () == 'solid state drive' : 
    print ('correct answer')
    score += 1

else : 
    print ('wrong answer') 

print (f"you get {score} correct answers")
print (f"you get {(score/questions)*100} %")

