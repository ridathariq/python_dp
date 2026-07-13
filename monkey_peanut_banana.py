n = int(input())
m = int(input())
p = int(input())
j = int(input())
k = int(input())  


if n <= 0 or m <= 0 or p <= 0 or j < 0 or k < 0:
    print("INVALID")

else:
    banana_ate = j // m
    peanut_ate = k // p
    total_ate = banana_ate + peanut_ate

    if total_ate > n:
        total_ate = n


    monkey_left = n - total_ate

    print("monkeys left is : " + str(monkey_left))

