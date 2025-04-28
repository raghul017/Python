def reverse(num):
    num = int(num)
    num1 = 0
    while num != 0:
        digit = num % 10
        num1 = num1 * 10 + digit
        num = num // 10
    return num1

inp = input("Enter the number: ")
ans = reverse(inp)
print(ans)