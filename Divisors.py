N=int(input("Enter a number:"))
count=0
for i in range(1,N+1):
    if (N%i)==0:
        count=count+1
print("The number of divisors of",N, "is",count)


