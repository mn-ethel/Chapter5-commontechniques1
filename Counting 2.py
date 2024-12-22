count1=0
count2=0

for i in range(1,101):
    square=i*i
    print (square)
    F=square%10
    if F==9:
        count1=count1+1
    if F==4:
        count2=count2+1
print("The number of square numbers between 1 and 100 ending in 4 is",count2)
print("The number of square numbers between 1 and 100 ending in 9  is",count1)
