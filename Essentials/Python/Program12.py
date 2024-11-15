# WA function to find whether a given number is prime or not

def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count = count+1
    
    # print("no of factors: ",count)
    if(count == 2):
        print(f"{n} is a prime number")

# is_prime(22)

for i in range(1,21):
    is_prime(i)  # calling the function for each number from 1 to 20