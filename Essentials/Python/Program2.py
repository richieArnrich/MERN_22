# operators : +, -, *, /, %, **, //, ==, !=, >,
#             <, >=, <=

# arithmetice opertors
#  + - / % *

a = 10
b= 20
print(a + b)  # 30

print(b-a) # 10

c = 188
d = 10
print(c/d)

print(c%d)
print(c*d)

num1 = 88
num2 = 97
x = num1%10
y = num2%10
result = x*10 + y
print("third number: ",result)

a = input("Enter a number")
b = input("Enter second number")
c = input("Enter third number")

n1 = int(a)
n2 = int(b)
n3 = int(c)
result = (n1%10)*100 + (n2%10)*10 + (n3%10)
print(result)

# power of a number in python
# ** operator is used to find the power of a number
# 2**3 = 8
print(2**3) # 8