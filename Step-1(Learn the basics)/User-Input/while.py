# Print numbers from 1 to 10 using a while loop.

num = 1
while num <= 10:
    print(num)
    num +=1


# Print all even numbers between 1 and 20 using a while loop.
num = 0
while num <=20:
    if num%2 ==0:
        print(num)
    num +=1

# Sum all numbers from 1 to N (given by user) using a while loop.

N = int(input("Enter your number"))

i = 1
total = 0

while i <=N:
    total += i
    i+=1

print(total)