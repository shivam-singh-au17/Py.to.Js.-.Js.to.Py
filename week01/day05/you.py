# COMPOUND INTEREST
# Given the Principal Amount, Interest Percentage and Time calculate the compound interest.

# Note - Please write the formula of Compound interest in multi-line comments, and write the explanation of each variable in single line comment.


"""
The compound interest formula is
CI = p*(1 + i)**nt
"""

principal = 2000;       # this is the principal amount
rate = .08;        # This is the rate in percent annum
time = 5;       #This is the time in year
n = 12;       #n is the number of times that interest is compounded per unit t
intrestRate = rate / n;       # This is the intrest rate per year
compoundIntrest = principal * (1 + intrestRate) ** (n*time)
print(compoundIntrest)




# THE GAME OF LIES - II
# Suppose there are 4 persons playing a game. The result of a particular match is dependant on various strategies of AND and OR

# Note - First Write your result in comments by calculating it on your own and check it whether it matches by running the code.

# GAME-1

# True and !(False) and !(True) or True or False
# GAME-2

# False and True or !(False) and (!True or !False)
# GAME-3

# True and False and (!False or !False) and True 
# GAME-4

# !(False and !False or (False and !True or !True))




a =   True and False and (not True) or False;
print(a) # result = False

b = True or (not False) and (True or False);
print(b)  # result = True

c = False or (not True and not False) or True;
print(c)  # result = True

d = not (False and not False or (False and not True or not True))
print(d)  # result = True