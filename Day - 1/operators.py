meaning = 42
print("")

# if meaning > 10:
#     print("Right ON!")
# else:
#     print("Not Today")

# Ternary Operators

print("Right ON!") if meaning > 10 else print("Not Today")

# Python Operators
# Python has a set of built-in operators that you can use to perform operations on variables and values.
# These operators can be classified into several categories, including arithmetic, comparison, logical, assignment, bitwise, identity, and membership operators.

# Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations:
# Operator	    Description	                    Example
# +	        Addition	                        x + y
# -	        Subtraction	                    x - y
# *	        Multiplication	                x * y
# /	        Division	                        x / y
# %	        Modulus	                        x % y
# **	        Exponentiation	                x ** y
# //	        Floor division	                x // y

# Comparison Operators
# Comparison operators are used to compare two values:
# Operator	    Description	                    Example
# ==	        Equal	                        x == y
# !=	        Not equal	                    x != y
# >	            Greater than	                x > y
# <	            Less than	                    x < y
# >=	        Greater than or equal to	    x >= y
# <=	        Less than or equal to	        x <= y


# Python Assignment Operators:

# Assignment operators are used to assign values to variables:

# Operator	    Example	        Same As
# =	            x = 5	        x = 5
# +=	        x += 3	        x = x + 3
# -=	        x -= 3	        x = x - 3
# *=	        x *= 3	        x = x * 3
# /=	        x /= 3	        x = x / 3
# %=	        x %= 3	        x = x % 3
# //=	        x //= 3	        x = x // 3
# **=	        x **= 3	        x = x ** 3
# &=	        x &= 3	        x = x & 3
# |=	        x |= 3	        x = x | 3
# ^=	        x ^= 3	        x = x ^ 3
# >>=	        x >>= 3	        x = x >> 3
# <<=	        x <<= 3	        x = x << 3
# :=	        print(x := 3)	x = 3


# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	    Name	                        Example
# ==	        Equal	                        x == y
# !=	        Not equal	                    x != y
# >	            Greater than	                x > y
# <	            Less than	                    x < y
# >=	        Greater than or equal to	    x >= y
# <=	        Less than or equal to	        x <= y

# Python Logical Operators
# Logical operators are used to combine conditional statements:
# Operator	    Description	                    Example
# and	        Returns True if both statements are true	x < 5 and  x < 10
# or	        Returns True if one of the statements is true	x < 5 or x < 4
# not	        Returns True if the statement is false	not(x < 5 and x < 10)

# Python Identity Operators
# Identity operators are used to compare the memory locations of two objects:

# Operator	    Description	                    Example
# is	        Returns True if both variables are the same object	x is y
# is not	    Returns True if both variables are not the same object	x is not y

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
# Operator	    Description	                    Example
# in	        Returns True if a sequence with the specified value is present in the object	x in y
# not in	    Returns True if a sequence with the specified value is not present in the object	x not in y


# Python Bitwise Operators
# Bitwise operators are used to compare binary values:

# Operator	    Description	                    Example
# &	        AND	                        x & y
# |	        OR	                        x | y
# ^	        XOR	                        x ^ y
# ~	        NOT	                        ~x
# <<	        Zero fill left shift	        x << 2
# >>	        Signed right shift	        x >> 2


# Python Operator Precedence

# Operator	                            Description
# **	                                    Exponentiation
# ~ + -	                            Bitwise NOT; unary plus and minus
# * / % //	                        Multiplication, division, modulo and floor division
# + -	                                Addition and subtraction
# << >>	                            Bitwise shift operators
# &	                                    Bitwise AND
# ^ |	                                Bitwise XOR and OR
# < <= > >=	                        Comparison operators
# == !=	                            Equality operators
# =	                                    Assignment operators
# is is not	                        Identity operators
# in not in	                        Membership operators
# and or not	                        Logical operators
