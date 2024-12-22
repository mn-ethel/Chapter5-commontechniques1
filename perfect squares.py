count = 0
for num in range(1, 1001):

    if (int(num ** 0.5) ** 2 != num) and (int(num ** (1/3)) ** 3 != num) and (int(num ** 0.2) ** 5 != num):
        count += 1


print("The number of integers from 1 to 1000 that are not perfect squares, cubes, or fifth powers is: ",count)

