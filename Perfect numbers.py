for n in range(1, 10000):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    if n == sum_of_divisors:
        print(n)


