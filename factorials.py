n=int(input("Enter number:"))
result=1
if n<0:
    print("Invalid input!")
for i in range(1,n+1):
    result *=i
print("The factorial of " ,n, "is",result)

