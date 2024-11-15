# factors of n
n = input("enter a number to find factors")
n = int(n) # convert string to int
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i = i+ 1
