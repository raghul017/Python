def isPrime(num):
    if num <2:
        return False
    for i in range(2, num):
        if num % 2==0:
            return False
        else:
            return True


res = isPrime(6)
print("Is Prime Number" if res else "Is not Prime Number")




