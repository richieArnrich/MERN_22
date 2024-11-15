# sum of all even and odd natural numbers 1 - 10
# sum_even = 30
# sum_odd = 25

sum_even = 0
sum_odd = 0

i = 1
while(i<=10):
    if(i%2 == 0):
        # if number is even
        sum_even = sum_even + i
    else:
        # if not even then odd sum
        sum_odd = sum_odd + i
    # end of if-else
    i = i + 1
# end of while
print(f"sum of even = {sum_even}")
# fstring
print(f"sum of odd = {sum_odd}")