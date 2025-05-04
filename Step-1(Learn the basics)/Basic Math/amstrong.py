def isAmstrong(n):
    val = 0
    num = str(n)
    length = len(num)
    for i in range(length):
        cube =(int(num[i])**length)
        val = val +cube
    return val == n

result = isAmstrong(153)
print(result)