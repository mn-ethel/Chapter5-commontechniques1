import math
n=int(input("Enter number:" ))
harmonic_sum=sum(1/i for i in range(1,n+1))
ln=math.log(n)
difference=harmonic_sum-ln
if n<0:
    print("Please enter positive integer")
else :
    print(difference)



