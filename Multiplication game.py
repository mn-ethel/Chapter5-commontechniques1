for i in range(1,11):
    from random import randint
    num1=randint(1,10)
    num2=randint(1,10)
    answer=num1*num2
    print(f"Question{i},{num1}*{num2}=",end=" ")
    user_answer=int(input(" "))
    if user_answer==answer:
        print("That's right you got it!")
    else:
        print("oops! the correct answer is",answer)

