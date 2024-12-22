Guesses=[]
Score=0
for i in range(5):
    Guess=int(input(f"Enter guess {i+1}:"))
    Guesses.append(Guess)
    from random import randint
    W=randint(1,10)
    if Guess==W:
        Score +=10
    else:
        Score -=1
print("The final score is:",Score)