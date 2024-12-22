count=0
for i in range(1,101):
    square=i*i
    print (square, sep =" ")
    R=square%10
    if  R==1 :
      count=count+1
print("The number of square numbers between 1 and 100 ending in one is",count)

