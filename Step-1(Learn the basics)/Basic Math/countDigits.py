def countDigits(n):
    count = 0
    while n!=0:
        n = n // 10
        count+=1
    return count
inp = int(input("Enter the number :"))
ans = countDigits(inp)
print(ans)