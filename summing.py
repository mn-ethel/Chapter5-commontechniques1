sum_total=0
n=2000
for i in range (1,n+1):
    if i%2==0:
        sum_total = sum_total + (-i)
    elif i%2==1:
        sum_total=sum_total +i
print("The result is",sum_total)








