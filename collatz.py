def collatz(x):
    if x % 2 == 0:
        x = x / 2
        if x == 1:
            return 1
        else:
            return 1 + collatz(x)
    else:
        x = (3 * x) + 1
        if x == 1:
            return 1
        else:
            return 1 + collatz(x)

n = int(input("Number: "))
print(collatz(n))