def isPalindrome(n):
    number = str(n)
    # reverse = number[::-1] #method1
    reverse = ''.join(reversed(number)) #method 2
    if number == reverse:
        return True


result = isPalindrome(1231)
print("Palindrome" if result else "Not Palindrome")