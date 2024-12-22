number = int(input("Enter a number: "))

is_square_free = True
for i in range(2, int(number ** 0.5) + 1):
    if (i * i) <= number and number % (i * i) == 0:
        is_square_free = False
        break

if is_square_free:
    print(number, "is a square-free number.")
else:
    print(number,"is NOT a square-free number.")
