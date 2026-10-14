def palindrome(x):
    if len(x) == 0:
        return True
    if x[0] == x[len(x) - 1]:
        return palindrome(x[1:-1])
    else:
        return False

n = input("Palindrome: ")
print(palindrome(n))