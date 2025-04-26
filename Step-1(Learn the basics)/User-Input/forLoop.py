# Print numbers from 1 to 10 using a for loop.

for i in range(11):
    if i==0:
        continue
    else:
        print(i)

#Print all even numbers from 1 - 100

for i in range(101):
    if(i%2==0):
        print(i)
    else:
        continue


lst = [10 , 20 , 30 , 40 , 50 ]

# print the elements in the list
for item in lst:
    print(item)

# .	Find the sum of all elements in a list using a for loop.
val = 0
for i in lst:
    val +=i
print(val)


# Find the maximum element in a list using a for loop (without using max()).
max = 0
for i in lst:
    if i > max:
        max = i
    else:
        continue
print(max)

# Reverse a list using a for loop (without using built-in reverse functions).
new_arr = []
for i in range(len(lst)-1 ,-1, -1):
    new_arr.append(lst[i])

print(new_arr)